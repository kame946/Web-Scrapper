import csv
import sqlite3
import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://www.theverge.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
articles = soup.find_all('article', class_='c-entry-box--compact__body')

headers = ['id', 'URL', 'headline', 'author', 'date']

filename = datetime.datetime.now().strftime('%d%m%Y') + '_verge.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    id_counter = 1
    for article in articles:
        headline = article.find('h2', class_='c-entry-box--compact__title').text.strip()
        url = article.find('a', class_='c-entry-box--compact__image-wrapper')['href']
        metadata = article.find('div', class_='c-byline').text.strip()
        author = metadata.split(' ')[0]
        date = metadata.split(' ')[-1]
        writer.writerow([id_counter, url, headline, author, date])
        id_counter += 1


dbname = datetime.datetime.now().strftime('%d%m%Y') + '_verge.db'
conn = sqlite3.connect(dbname)
conn.execute('''
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY,
    url TEXT,
    headline TEXT,
    author TEXT,
    date TEXT
)
''')

for article in articles:
    headline = article.find('h2', class_='c-entry-box--compact__title').text.strip()
    url = article.find('a', class_='c-entry-box--compact__image-wrapper')['href']
    metadata = article.find('div', class_='c-byline').text.strip()
    author = metadata.split(' ')[0]
    date = metadata.split(' ')[-1]
    conn.execute('INSERT INTO articles (id, url, headline, author, date) VALUES (?, ?, ?, ?, ?)', (id_counter, url, headline, author, date))
    id_counter += 1

conn.commit()
conn.close()
