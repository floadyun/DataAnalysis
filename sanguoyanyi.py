from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba

#剔除重复性高无意义的关键词
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "主公", "军士", "左右", "军马", "引兵", "次日", "大喜", "天下", "东吴",
            "于是", "今日", "不敢", "魏兵", "人马", "陛下", "一人", '不知', '蜀兵', '何故', ''}

# 从百度百科下载的文中的人物名字，并筛选出重复的名字，保存在列表里
print('读取出场人物数据.....')
with open('file\sanguo_name.txt', 'r', encoding='utf-8') as f:
    names = list(set(name.strip() for name in f.readlines()))
print('读取文本内容......')
sanguo_text = open('file\三国演义.txt', 'r', encoding='UTF-8').read()

# 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
# cut_text = " ".join(jieba.cut(sanguo_text))
words = jieba.cut(sanguo_text)
counts = {}
sanguo = ''
for word in words:
    if len(word) == 1:
        continue
    elif word == "孔明" or word == "孔明曰":
        rword = "诸葛亮"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word =='翼德':
        rword = '张飞'
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "操":
        rword = "曹操"
    else:
        rword = word
    if names.__contains__(rword):
        sanguo = sanguo + ',' + rword
        counts[rword] = counts.get(rword, 0) + 1
# for word in excludes:
#     del(counts[word])

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(len(items)):
    word, count = items[i]
    print(word, count)

cloud_img = imread('image\guanyu.jpg')
wordcloud = WordCloud(font_path='file\BLPP.ttf', mask=cloud_img, max_words=10).generate_from_text(sanguo)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()