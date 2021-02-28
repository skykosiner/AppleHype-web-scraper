import requests
import csv
from bs4 import BeautifulSoup 
from datetime import date
# Source to the page to get infomation from
source = requests.get("https://www.applehype.com/").text
soup = BeautifulSoup(source, "lxml")
# File to write to 
csv_file = open ('Apple hype listing.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writ6
# What to look for on the website
html = soup.find("html")
# App recommendation
App = html.find("div", id="block-4e0ba45936df4db9470a").text
for link in soup.find_all('a'):
    print(link.get('href'))
# Accessory recomendation
Accessory = html.find("div", id="block-a1664f8f69b13bdf11ac").text
# Apple news
News = html.find("div", id="block-1194675c2533d5ee7da5").text
# Date 
today = date.today()


print(today)
print(App)
print(Accessory)
print(News)

csv_writer.writerow([today, App, Accessory, News])

csv_file.close( )
