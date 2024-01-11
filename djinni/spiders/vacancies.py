import scrapy
from scrapy.http import Response
import datetime

from djinni.spiders.config import KEYWORDS, MONTHES


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response) -> dict[str]:
        pages = [
            response.urljoin(self.start_urls[0] + f"&page={i}")
            for i in range(
                int(
                    response.css(
                        ".pagination > .page-item > a::text"
                    ).getall()[-3]
                )
            )
        ]

        for page in pages:
            yield scrapy.Request(page, callback=self._parse_single_page)

    def _parse_single_page(self, response: Response, **kwargs) -> dict[str]:
        for vacancy in response.css(".job-list__item"):
            detailed_url = response.urljoin(
                vacancy.css(".job-list-item__link::attr(href)").get()
            )
            info = vacancy.css(
                ".job-list-item__job-info > .nobr::text"
            ).getall()
            try:
                info.remove("Product")
            except ValueError:
                pass
            location = ", ".join(
                [
                    loc.strip()
                    for loc in vacancy.css(".location-text::text")
                    .get()
                    .replace(",", " ")
                    .split()
                ]
            )
            experience = info[1].split()[0]
            if not experience.isnumeric():
                experience = 0
            else:
                experience = int(experience)
            vacancy_data = {
                "title": vacancy.css(
                    ".job-list-item__link::text"
                ).get().strip(),
                "location": location,
                "type": info[0],
                "experience": experience,
                "english": info[2] if len(info) > 2 else None,
            }
            yield scrapy.Request(
                detailed_url,
                callback=self._parse_detail,
                meta={"vacancy_data": vacancy_data},
            )

    def _parse_detail(self, response: Response, **kwargs) -> dict[str]:
        page_data = response.css(".job-post-page > div.row")
        vacancy_info = [
            s.strip()
            for s in page_data.css(".text-small > .text-muted::text").extract()
        ]
        description = " ".join(page_data.css("::text").getall()).lower()
        keywords = [
            KEYWORDS[key]
            for key in KEYWORDS.keys()
            if any(word in description for word in key)
        ]
        date = vacancy_info[1].split()[2::]
        for keyword in keywords:
            yield {
                "technology": keyword,
                **response.meta["vacancy_data"],
                "datetime": datetime.date(
                    year=int(date[2]), month=MONTHES[date[1]], day=int(date[0])
                ),
                "views": int(vacancy_info[3].split()[0]),
                "applicants": int(vacancy_info[4].split()[0]),
            }
