import requests # lets us fetch data from a website
from bs4 import BeautifulSoup # helps us read and search through html code
import csv # built-in module for working with CSV files

page = 1
all_quotes = [] # we'll collect all quotes into this list of dictionaries

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    print(f"Scraping page {page}...") # visual feedback
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if len(quotes) == 0:
        print("No more quotes found. Done scraping!")
        break # this stops the loop if no quotes are found

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
    writer.writeheader() # add column titles
    writer.writerows(all_quotes)

print("Quotes saved to quotes.csv")