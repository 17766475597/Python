# coding = utf-8
import requests
from bs4 import BeautifulSoup as bs
import re
import time
import json


# 访问我的博客
def spider(url, headers):
    r = requests.get(url=url, headers=headers)
    html = r.text
    # 解析html代码
    soup = bs(html, 'lxml')
    # print(soup);
    # ul = soup.find(name='ul', attrs={'class': 'mod_my_t clearfix'})
    ul = soup.find('div', attrs={'class': 'grade-box'})
    # uli=ul.find_next_siblings('li')
    # print(ul);
    # 查看bs4的文档 find 方法 查找元素，find_next_siblings获取兄弟元素
    text = ul.find("dt", text="访问：").find_next_siblings();

    print(text);

    t = text[0];
    print(t)
    # 将Tag元素转为字符串
    t3 = str(t);
    # 上面的find是bs4的方法，这里的是字符串的find
    t0 = t3.find("title=", 0, len(t3))
    t1 = t3.find(">", 0, len(t3))

    print(t0);
    print(t1);
    # 截取数字
    numbers = t3[t0 + 7:t1 - 1];
    print(numbers);
    # 将字符串类型转列表
    numbers = numbers.split(" ")
    # text1=soup.find_all("dt", text="访问：")
    # print(text1);
    # 获取当前年月日
    date = time.strftime("%Y-%m-%d", time.localtime())
    # 拼接日期
    numbers.append(date)
    text_save(numbers, 'raningDate.txt')
    print('成功执行!')


# 文件存储
def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        # 如果索引为最后一位，去掉空格且拼上换行符，否则剩下的后面拼接逗号
        if i == len(content) - 1:
            number = (content[i]) + '\n'
        else:
            number = str(content[i]) + ','
        file.write(number)
    file.close()


if __name__ == '__main__':
    url = "https://blog.csdn.net/ruiti/article/details/82715601"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'blog.csdn.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    spider(url, headers)
