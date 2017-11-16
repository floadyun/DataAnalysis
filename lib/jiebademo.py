import jieba

def testCut():
    cutStr = '中华人民共和国今天成立了'
    # 全模式
    seg_list = jieba.cut(cutStr, cut_all=True)
    print('全模式:'+'/'.join(seg_list))

    #精准模式
    seg_list2 = jieba.cut(cutStr, cut_all=False)
    print('精准模式:'+'/'.join(seg_list2))

    #搜索引擎模式
    seg_list3 = jieba.cut_for_search(cutStr)
    print('搜索引擎模式:'+'/'.join(seg_list3))