import requests
from bs4 import BeautifulSoup
import os
os.system('clear')
channel = input("Enter channel :")
if channel=="":
    channel='ryans world'
url = {'ryans world':"https://www.youtube.com/channel/UChGJGhZ9SOOHvBB0Y4DOO_w",'troom troom':""}
a = requests.get(url[f'{channel}']).text
count = 0
soup = BeautifulSoup(a,'lxml')
titles = soup.findAll('a')
times = soup.findAll('span',class_ = "accessible-description")

for title in titles:
    try:
        if count==5:
            break
        if title['title'] and title['aria-describedby']:
            print(title.text,times[count].text,end="\n"*2)
            count+=1

        if count==5:
            break

    except Exception:
        pass