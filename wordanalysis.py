# -*- coding: utf-8 -*-
def drawWordCloud(text_url, mask_url):
    import jieba
    from scipy.misc import imread
    import matplotlib.pyplot as plt
    from progressbar import ProgressBar

    from wordcloud import WordCloud, ImageColorGenerator
    with open(text_url, 'r', encoding='utf-8') as f:
        all_chaps = [chap for chap in f.readlines()]

    pbar = ProgressBar()
    # 给整本书分词
    dictionary = []
    for i in pbar(range(len(all_chaps))):
        # print "处理第{}回".format(i+1)
        words = list(jieba.cut(all_chaps[i]))
        dictionary.append(words)

    # 摊平
    tmp = []
    for chapter in dictionary:
        for word in chapter:
            tmp.append(word)
    dictionary = tmp

    # 过滤掉重复的词语
    unique_words = list(set(dictionary))

    # test_text = [(u'林黛玉',10), (u'贾宝玉', 20), (u'宝钗', 8)]
    #     pbar =ProgressBar(maxval=len(unique_words))
    freq = []
    for word in unique_words:
        freq.append((word, dictionary.count(word)))

    # sort
    freq.sort(key=lambda x: x[1], reverse=True)

    # broke_words
    broke_words = []
    with open('file\stopwords.txt', 'r', encoding='utf-8') as f:
        broke_words = [i.strip() for i in f.readlines()]

    # 除去broke_words
    freq = [i for i in freq if i[0] not in broke_words]

    # 除去单音节词
    freq = [i for i in freq if len(i[0]) > 1]

    img_mask = imread(mask_url)
    img_colors = ImageColorGenerator(img_mask)

    wc = WordCloud(background_color="white",  # 背景颜色max_words=2000,# 词云显示的最大词数
                   font_path='file\BLPP.ttf',
                   mask=img_mask,  # 设置背景图片
                   max_font_size=60,  # 字体最大值
                   random_state=42)

    wc.fit_words(freq)

    plt.imshow(wc)
    plt.axis('off')
    plt.show()