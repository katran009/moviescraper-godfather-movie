from bs4 import BeautifulSoup
import requests

url = "https://www.rottentomatoes.com/m/godfather"
res = requests.get(url)
soup = BeautifulSoup(res.text)

title = soup.select(".scoreboard__title")
print(title)

release_year = soup.select(".scoreboard__info")
print(release_year)

critic_score = soup.select(".scoreboard__link--tomatometer")
print(critic_score)

user_score = soup.select(".scoreboard__link--audience")
print(user_score)
