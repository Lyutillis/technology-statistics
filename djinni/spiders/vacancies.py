import scrapy
import re
from scrapy.http import Response
import locale
import datetime
from dateutil import parser

from djinni.spiders.utils import KEYWORDS, MONTHES


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response):
        for vacancy in response.css(".job-list__item"):
            detailed_url = response.urljoin(
                vacancy.css(".job-list-item__link::attr(href)").get()
            )
            info = vacancy.css(".job-list-item__job-info > .nobr::text").getall()
            try:
                info.remove("Product")
            except ValueError:
                pass
            location = ", ".join([loc.strip() for loc in vacancy.css(".location-text::text").get().replace(",", " ").split()])
            vacancy_data = {
                "title": vacancy.css(".job-list-item__link::text").get().strip(),
                "location": location,
                "type": info[0],
                "experience": info[1],
                "english": info[2] if len(info) > 2 else None,
            }
            yield scrapy.Request(
                detailed_url,
                callback=self._parse_detail,
                meta={"vacancy_data": vacancy_data}
            )

        next_page = response.css(".pagination > .page-item")[-1]

        if next_page.css("span").get() is not None:
            next_page_url = response.urljoin(next_page.css("::attr(href)").get())
            yield scrapy.Request(next_page_url, callback=self.parse)

    def _parse_detail(self, response: Response, **kwargs) -> dict[str]:
        page_data = response.css(".job-post-page > div.row")
        vacancy_info = [s.strip() for s in page_data.css(".text-small > .text-muted::text").extract()]
        keywords = [key for key in KEYWORDS if key in page_data.get().lower()]
        date = vacancy_info[1].split()[2::]
        for keyword in keywords:
            yield {
                "technology": keyword,
                **response.meta["vacancy_data"],
                "datetime": datetime.date(year=int(date[2]), month=MONTHES[date[1]], day=int(date[0])),
                "views": int(vacancy_info[3].split()[0]),
                "applicants": int(vacancy_info[4].split()[0]),
            }
