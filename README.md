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

3. Create a new branch:
`git checkout -b <new branch name>`

4. Create virtual environment:
`python3 -m venv venv`

5. Acivate venv:
`source venv/Scripts/activate`

6. Install requirements:
`pip3 install -r requirements.txt`

7. Scrape Data from "Djinni":
`scrapy crawl vacancies -O technologies.csv`

8. Run the main.ipynb Jupyter Notebook cells.

Now you can overwiev the statistics.

# Examples
