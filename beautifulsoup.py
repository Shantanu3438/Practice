from bs4 import BeautifulSoup as bs
import requests

site = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
siteSoup = bs(site.text, 'html.parser')
tags = siteSoup.find_all('a')
releaseDate = siteSoup.find_all('span', class_ = 'secondaryInfo')
movieTitle = siteSoup.select('td a', class_ = 'titleColumn')
for i in range(250):
    print(movieTitle[i].text + releaseDate[i].text)