from bs4 import BeautifulSoup as bs
import requests
import files
from qbittorrent import Client

qb = Client("http://127.0.0.1:8080/")
qb.login("admin", "adminadmin")

site = requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")
print(site.text)
siteSoup = bs(site.text, 'html.parser')
releaseDate = siteSoup.find_all('span', class_ = 'secondaryInfo')
movieTitle = siteSoup.select('td a', class_ = 'titleColumn')
movieList = open('tv.txt', 'w')
for movie in movieTitle:
    #print(movie.text)
    movieList.write(movie.text)
    
movieList.close()

movieFile = open('tv.txt')
movieList = movieFile.read().splitlines()

for movie in movieList:
    if movie == ' ':
        print('empty')
        continue
    movieLink = "https://pbays.top/search/" + movie + "/1/99/0"
    print(movieLink)
    movieSite = requests.get(movieLink)
    movieSoup = bs(movieSite.text, 'html.parser')
    movieMagnetLink = movieSoup.find("a", {'title' : 'Download this torrent using magnet'})
    print(movieMagnetLink.attrs['href'])
    magnetLink = movieMagnetLink.attrs['href']
    #print(magnetLink)
    qb.download_from_link(magnetLink)