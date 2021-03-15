import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

godfather_url = "https://www.rottentomatoes.com/m/godfather"
driver.get(godfather_url)

sug_html = driver.get('innerHTML')
print(sug_html)


title = [x.text for x in soup.find_all('span', { "class" : "scoreboard_title" })]
release_year = [x.text for x in soup.find_all('span', { "class" : "scoreboard_info" })]
critic_score = [x.text for x in soup.find_all('div', { "class" : "scoreboard__link scoreboard__link--tomatometer" })]
user_score = [x.text for x in soup.find_all('div', { "class" : "scoreboard__link scoreboard__link--audience" })]
link = [x['href'] for x in soup.find_all('a')]

suggested_movies = zip(title,release_year, critic_score, user_score, link[:-1])
