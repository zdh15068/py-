import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109'
}
def IMGbz():
    num = 1
    for page in range(1,10):
        print('=======正在爬取第{}页的数据======='.format(page))
        url = 'http://acg17.com/category/meitu/pixiv-painter/page/{}/'.format(page)
        response = requests.get(url=url,headers=headers)
        response.encoding = response.apparent_encoding
        # 需要使用xpath
        Etree = etree.HTML(response.content)
        # 获取到每一页的html
        html = Etree.xpath('//article/h2/a/@href')
        for img_html in html:
            response2 = requests.get(url=img_html,headers=headers)
            Etree2 = etree.HTML(response2.content)
            # 获取到每一页的图片数据
            img_url = Etree2.xpath('//*[@id="the-post"]/div/div/p/img/@src')
            for imgs_url in img_url:
                response_img = requests.get(url=imgs_url,headers=headers)
                with open(r'E:\photos\{}.jpg'.format(num),'wb') as f:
                    print('正在爬取数据------',num)
                    f.write(response_img.content)
                    num += 1
                    f.close()
IMGbz()
