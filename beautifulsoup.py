from bs4 import BeautifulSoup as bs
import requests
import files
import qbittorrentapi

conn_info = dict(
    host="localhost",
    port=8080,
    username="admin",
    password="adminadmin",
)
qbt_client = qbittorrentapi.Client(**conn_info)
qbt_client.auth_log_in()

site = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
siteSoup = bs(site.text, 'html.parser')
releaseDate = siteSoup.find_all('span', class_ = 'secondaryInfo')
movieTitle = siteSoup.select('h3', class_ = 'ipc-title__text')
print(movieTitle)
movieList = open('movieList.txt', 'w')
releaseDateList = open('releaseDate.txt', 'w')
for i in range(len(releaseDate)):
    #fullTitle = movieTitle[i].text + releaseDate[i].text
    movieList.write(movieTitle[i].text)
    releaseDateList.write(releaseDate[i].text + '\n')

    
movieList.close()

movieFile = open('movieList.txt')
movieList = movieFile.read().splitlines()

for movie in movieList:
    if movie == ' ':
        continue
    movieLink = "https://pbays.top/search/" + movie + "/1/99/0"
    movieSite = requests.get(movieLink)
    movieSoup = bs(movieSite.text, 'html.parser')
    movieMagnetLink = movieSoup.find("a", {'title' : 'Download this torrent using magnet'})
    if movieMagnetLink is not None:
        magnetLink = movieMagnetLink.attrs['href']
        qbt_client.torrents_add(magnetLink)
qbt_client.auth_log_out()
