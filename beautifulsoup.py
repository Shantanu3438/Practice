from bs4 import BeautifulSoup as bs
import requests
import files
from qbittorrent import Client

qb = Client("http://127.0.0.1:8080/")
qb.login("admin", "adminadmin")

site = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
siteSoup = bs(site.text, 'html.parser')
tags = siteSoup.find_all('a')
releaseDate = siteSoup.find_all('span', class_ = 'secondaryInfo')
movieTitle = siteSoup.select('td a', class_ = 'titleColumn')
movieList = open('movieList.txt', 'w')
for movie in movieTitle:
    movieList.write(movie.text)

movieList.close()

movieFile = open('movieList.txt')
movieList = movieFile.read().splitlines()

for movie in movieList:
    movieLink = "https://pbays.top/search/" + movie + "/1/99/0"
    print(movieLink)
    movieSite = requests.get(movieLink)
    movieSoup = bs(movieSite.text, 'html.parser')
    movieMagnetLink = movieSoup.select("a[title = 'Download this torrent using magnet']")
    print(movieMagnetLink)
    #magnetLink = movieMagnetLink[1].attrs['href']
    #print(magnetLink)
    #qb.download_from_link(magnetLink)