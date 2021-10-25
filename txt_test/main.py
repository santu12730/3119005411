from methon import *
import sys

if __name__ == "__main__":
    str1 = methon.get_contents(sys.argv[1])
    str2 = methon.get_contents(sys.argv[2])
    text1 = methon.filter(str1)
    text2 = methon.filter(str2)
    similarity = methon.calc_similarity(text1, text2)
    print("文章相似度： %.2f" % similarity)
    # 将相似度结果写入指定文件
    f = open(sys.argv[3], 'w', encoding="utf-8")
    f.write(sys.argv[1][11:] + '  和  ' + sys.argv[2][11:] + '\n' + "文章相似度： %.2f" % similarity)
    f.close()
