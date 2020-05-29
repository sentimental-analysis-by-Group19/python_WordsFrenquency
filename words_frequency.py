import jieba
def word_frequency() :
    f1 = open("评论汇总.txt","r",encoding="utf-8")
    txt = f1.read()
    words = jieba.lcut(txt, cut_all=False)
    counts = {}
    for word in words:
        #排除词数为1的词语
        if len(word)==1:
            continue
        else:
            counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(100):
        word,count = items[i]
        print( "{0:<10}{1:>5}".format(word,count) )
    f1.close()
    #将词频结果存入文件
    f2 = open("words_frequency.txt", 'w', encoding='utf-8')  # 以'w'方式打开文件
    for k, v in items:  # 遍历字典中的键值
        s1 = str(k)  # 把字典的键转换成字符型
        s2 = str(v)
        f2.write(s1 + ' ')  # 键和值放在一行，用空格分开
        f2.write(s2+ '\n')
    f2.close()
word_frequency()