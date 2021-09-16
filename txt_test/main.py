import re
import sys

import gensim
import jieba


# 获取指定路径的文件内容
def get_contents(path):
    str = ''
    afile = open(path, 'r', encoding='UTF-8')
    line = afile.readline()
    while line:
        str = str + line
        line = afile.readline()
    afile.close()
    return str


# 将读取到的文件内容先进行jieba分词，然后再把标点符号、转义符号等特殊符号过滤掉
def filter(str):
    str = jieba.lcut(str)
    result = []
    for tags in str:
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags):
            result.append(tags)
        else:
            pass
    return result


# 传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text_1, text_2):
    texts = [text_1, text_2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    a_similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text_1)
    cosine_sim = a_similarity[test_corpus_1][1]
    return cosine_sim


if __name__ == '__main__':
    path1 = sys.argv[1]  # 论文原文的文件的绝对路径（作业要求）
    path2 = sys.argv[2]  # 抄袭版论文的文件的绝对路径
    path3 = sys.argv[3]  # 输出结果绝对路径
    str1 = get_contents(path1)
    str2 = get_contents(path2)
    text1 = filter(str1)
    text2 = filter(str2)
    similarity = calc_similarity(text1, text2)
    print("文章相似度： %.2f" % similarity)
    # 将相似度结果写入指定文件
    f = open(path3, 'w', encoding="utf-8")
    f.write(sys.argv[1]+sys.argv[2]+"文章相似度： %.2f" % similarity)
    f.close()
