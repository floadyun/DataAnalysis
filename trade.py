from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

soup = BeautifulSoup(open("s526398.htm", 'r', encoding='utf-8'), 'lxml')
trs = soup.find_all('tr', attrs={'align': "right", 'bgcolor':''})
symbols = []
direction = []
# print(trs)
for tr in trs:
    tds = tr.contents
    if len(tds) > 5:
        direction.append(tds[2].string)
        print(tds[4].string)
        symbol = tds[4]
        symbols.append(tds[4].string)