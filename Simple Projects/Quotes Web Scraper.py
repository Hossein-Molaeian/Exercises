import bs4
import requests

base_url = "http://quotes.toscrape.com/page/{}/"

authors_set = set()
page_number = 1

while True:

    scrape_url = base_url.format(page_number)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    if "No quotes found!" in res.text:
        break

    authors_soup = soup.select(".author")

    for author in authors_soup:
        authors_set.add(author.text)

    page_number += 1

print(authors_set)
