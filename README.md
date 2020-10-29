# NPL_unionNews_WordCloud
unionNews_WordCloud 新聞雲

網頁爬蟲應用  

jieba、wordcloud 模組應用  

# 程式執行：
1. 執行主程式unionNews.py
2. 爬蟲爬取每則新聞網址後，取得所有新聞內容，運用"jieba"模組設定詞庫、停用詞、拆解字詞，存入terms[]陣列
3. diction = Counter(terms) 取得拆解後的每個字詞出現次數
4. wordcloud 模組，設定文字雲字型、文字雲形狀(heart.png)、背景顏色，最後產生文字雲
5. matplotlib 模組產生圖片
6. 最後 wordcloud.to_file("union_WordCloud.png") 存檔
7. get_newUrl.py -- re_url(url)  
   處理新聞連結出錯問題:  
   一. 原網址get後爬取不到資料內容，因為會產生新網址與原網址不同，重新爬取取得新網址
   二. 有的新聞只有會員才可讀取

# 執行結果文字雲圖：
![image](https://github.com/KAIHSU74/NPL_unionNews_WordCloud/blob/main/union_WordCloud.png)
