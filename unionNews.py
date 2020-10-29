import requests
from bs4 import BeautifulSoup as soup
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter
from fake_useragent import UserAgent
import time
from random import randint
from get_newUrl import re_url

ua = UserAgent()
headers = {'User-Agent': ua.random}

urls = []
# 1頁 20則新聞, 設定前 60則(前3頁)
for p in range(1,4):
    # 取得聯合報即時新聞每筆連結
    url = 'https://udn.com/api/more?page='+str(p)+'&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=10351'
    html = requests.get(url, headers=headers).json()
    for i in range(len(html['lists'])):
        url = html['lists'][i]['titleLink']
        urls.append("https://udn.com"+url)
    
# 取得新聞內容
errUrl = []
text_news = ''
i = 1
for url in urls:
    html = requests.get(url, headers=headers)
    objsoup = soup(html.text, 'lxml')
    try:
        findp = objsoup.find("article",class_="article") or \
                objsoup.find("article",class_="article-content") or \
                objsoup.find("div", id="container") or \
                objsoup.find("div",class_="container") or \
                objsoup.find("div",class_="articleMain")
        if findp: 
            allptag = findp.find_all("p")
            print('處理 {0} 新聞內容'.format(url))
            for p in allptag:
                t = p.text.rstrip()
                t = t.replace('\n\r','').replace('\n','').replace('\r','')
                if t != '':
                    text_news += t
        print('已完成數: ', i)
        i += 1
        time.sleep(randint(0,2))
    except Exception as e:
        errUrl.append(url)
        text_news += re_url(url)
        print('已完成數: ', i)
        i += 1
        next
for u in errUrl:
    print(u)
      
jieba.set_dictionary('dict.txt.big.txt')
# 設定停用詞
with open('stopWord_union.txt','r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')

terms = []
for t in jieba.cut(text_news, cut_all=False):
    if t not in stops:
        terms.append(t)
diction = Counter(terms)
#for d in diction.keys():
#    print(d)
font = r'msyh.ttc'                          # 設定字詞
mask = np.array(Image.open('heart.png'))    # 設定文字雲形狀
unioncloud = WordCloud(font_path=font, background_color="white", mask=mask)     # 設定背景顏色為白色
unioncloud.generate_from_frequencies(frequencies=diction)                       # 產生文字雲

# 產生圖片
plt.figure(figsize=(6,6))
plt.imshow(unioncloud)
plt.axis("off")
plt.show()

unioncloud.to_file('union_WordCloud.png')   # 存檔