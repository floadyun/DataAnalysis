# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt

def drawWordCloud(text_url, img_url):
    print('读取文本内容......')
    word_text = open(text_url, 'r', encoding='UTF-8').read()
    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    cut_text = " ".join(jieba.cut(word_text))

    cloud_img = imread(img_url)
    wordcloud = WordCloud(background_color='white', font_path='file\BLPP.ttf', max_words=10, mask=cloud_img).generate_from_text(cut_text)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()