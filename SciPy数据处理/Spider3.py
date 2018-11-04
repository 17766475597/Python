from bs4 import BeautifulSoup
import requests

def Spider(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    meta = soup.find('div',attrs={'id':'wrapper'})
    name = meta.find('span')
    namestr = str(name)
    t0 = namestr.find('>')
    t1 = namestr.find('/span')
    name = namestr[t0+1:t1-1]
    print("作品名称：",name)

    d1 = soup.find('div',attrs={'id':'info'})
    author = d1.find('a')
    author1 = str(author)
    t0 = author1.find(']')
    t1 = author1.find('<',2)
    author = author1[t0+1:t1]
    print("作者：",author.strip())

    d1 = soup.find('div', attrs={'id': 'info'})
    author = d1.find('a')
    author1 = str(author)
    t0 = author1.find('[')
    t1 = author1.find(']', 2)
    author = author1[t0 + 1:t1]
    print("国籍：", author.strip())

    d = soup.find_all('div',attrs={'class':'intro'})

    d2 = d[0]
    ai = d2.find('p')
    ai1 = str(ai)
    t0 = ai1.find('<')
    t1 = ai1.find('<\p>')
    ai = ai1[t0+3:t1-3]
    print("简介：",ai)

    d2 = d[1]
    ai = d2.find('p')
    ai1 = str(ai)
    t0 = ai1.find('<')
    t1 = ai1.find('<\p>')
    ai = ai1[t0 + 3:t1 - 3]
    print("作者简介：", ai)

    d3 = soup.find_all('p',attrs={'class':'comment-content'})
    for ele in d3:
        com = ele.find('span')
        # print(com)
        com1 = str(com)
        t0 = com1.find('>')
        t1 = com1.find('</span>')
        com = com1[t0+1:t1]
        print(com)


url = 'https://book.douban.com/subject/1058661/'
Spider(url)