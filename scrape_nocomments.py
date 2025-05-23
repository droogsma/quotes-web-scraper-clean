import requests
from bs4 import BeautifulSoup
import csv

page = 1
all_quotes = []

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    print(f"Scraping page {page}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if len(quotes) == 0:
        print("No more quotes found. Done scraping!")
        break

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()

        all_quotes.append({
            "quote": text,
            "author": author
        })

    page += 1

with open("quotes.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)

print("Quotes saved to quotes.csv")