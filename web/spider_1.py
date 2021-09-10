#!/usr/bin/env python
# coding=utf-8
import urllib.request
import os
page = 0
count = 0
def open_url(url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0')
    responce = urllib.request.urlopen(request)
    html = responce.read()
    return html
def next_page_url(url):
    html = open_url(url).decode('utf-8')
    a = html.find('data-pagination="next" href=')
    b = html.find('><span class',a)
    return html[a + 29:b - 2]

def get_imgs(url):
    global count
    global page
    print('------正在获取第%d页的内容---------' % page)
    html = open_url(url).decode('utf-8')
    img_source_url = []
    a = html.find('img src="')
    while a != -1:
        b = html.find('jpg',a,a + 255)
        if b != -1:
            img_source_url.append(html[a + 9:b + 3])
        else:
            b = a + 9
        a = html.find('img src="',b)
    for each in img_source_url:
        filename = each.split('/')[-1]
        if os.path.isfile(filename):
            continue
        with open(filename,'wb') as f:
            f.write(open_url(each))
            count += 1
            print('-----------程序仍在运行，已下载%d张图片------' % count)

def download(url,pages = 500):#爬取前十页
    global page
    if not os.path.exists('resourse'):
        os.mkdir('resourse')
    os.chdir('resourse')
    for i in range(pages):
        page += 1
        print('-----------当前页码：%d -------' % page)
        try:
            get_imgs(url)
            url = next_page_url(url)
        except urllib.error.URLError:
            break
    print("抓取完毕！")


if __name__ =='__main__':
    try:
        download('https://233.fi/explore/trending/?list=images&page=1')
    except KeyboardInterrupt:
        print("程序已终止！")
