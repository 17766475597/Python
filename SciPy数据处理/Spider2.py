from bs4 import BeautifulSoup
import requests

def Spider(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    ul = soup.find('ul',attrs={'class':'hotArticle-list csdn-tracking-statistics tracking-click'})
    read = ul.find_all('p')
    str1 = str(read)
    str2 = str1.split(',')
    for ele in str2:
        t0 = ele.find('span')
        t1 = ele.find('/span')
        number = ele[t0+5:t1-1]
        print(number)



url = 'https://blog.csdn.net/ruiti/article/details/78870004'
Spider(url)