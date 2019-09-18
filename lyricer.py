import bs4
import requests

def getlyrics(url):
    # URL='https://genius.com/Snow-patrol-chocolate-lyrics'
    r= requests.get(url)
    soup=bs4.BeautifulSoup(r.content,'html5lib')
    print(soup.p.get_text())

def gsearch(song):
    song = song.replace(" ","+")
    gurl='https://www.google.com/search?q='+song+'+lyrics'
    r = requests.get(gurl)
    soup = bs4.BeautifulSoup(r.content,'html5lib')
    for s in soup.find_all("a"):
        if 'genius' in s.text:
            print(s.get('href')[7:].split('&')[0])
            return s.get('href')[7:].split('&')[0]
    return "P"

if __name__=="__main__":
    song =input("Enter name of song and artist:")
    #song="snow patrol chocolate"
    url = gsearch(song)
    print("*************************")
    getlyrics(url)
    print("*************************")