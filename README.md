# technology-statistics
This project combines web scraping with data-analysys.

In the "/djinni" folder there is a scraper written with Scrapy that creates dataset with info on all python-related vacancies.
The columns are: 
- `technology` - the name of technology present in vacancy description. The keywords are taken from dict in `/djinni/spiders/config.py`.
- `title` - The name of vacancy.
- `location` - Where the company is situated.
- `type` - Remote/Office.
- `experience` - Years of experience required to apply.
- `english` - Required english-level or None if not stated.
- `datetime` - Date when the vacancy was posted.
- `views` - Number of views.
- `applicants` - Number of applicants.

# Launching project locally
To run the project follow these steps:
1. Fork the repository

2. Clone it:
`git clone <here goes the HTTPS link you could copy on github repositiry page>`

3. Create virtual environment:
`python3 -m venv venv`

4. Acivate venv:
- MAC `source venv/Scripts/activate`
- Windows `cd venv/Scripts/activate` -> `. activate`

5. Install requirements:
`pip3 install -r requirements.txt`

6. Scrape Data from "Djinni":
`scrapy crawl vacancies -O technologies.csv`

7. Run the main.ipynb Jupyter Notebook cells.

Now you can overwiev the statistics.

# Examples
![image](https://github.com/Lyutillis/technology-statistics/assets/62535257/e278c4e8-3726-460b-80ac-a904408c00e9)
![image](https://github.com/Lyutillis/technology-statistics/assets/62535257/6de516e0-201e-47c3-8add-0cff4ffd6346)
![image](https://github.com/Lyutillis/technology-statistics/assets/62535257/8f29fe69-f7f0-4ad3-ad7f-dd49e21d9fa8)
![image](https://github.com/Lyutillis/technology-statistics/assets/62535257/6aacd522-147a-4a07-a676-0fe9d4900be0)

