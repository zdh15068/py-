import requests
from lxml import etree
import os
import urllib.parse
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64'
}
def get_bilibili(name):
    name = urllib.parse.quote(name)
    url = f'https://search.bilibili.com/all?keyword={name}'
    res = requests.get(url,headers=headers)
    # print(res.text)
    tree = etree.HTML(res.text)
    # 获取网页内视频链接
    url_list = tree.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li/div/div[1]/a/@href')
    for i in url_list:
        i = 'https:'+i
        print(i,end=' ')
        # 在当前目录创建
        path = './b站视频'
        os.system('you-get -o {} {}'.format(path,i))

if __name__ == '__main__':
    name = input('输入关键字：')
    get_bilibili(name)