import methon


def unit_test(path_1,path_2,path_3):
    str1 = methon.get_contents(path_1)
    str2 = methon.get_contents(path_2)
    text1 = methon.filter(str1)
    text2 = methon.filter(str2)
    similarity = methon.calc_similarity(text1, text2)
    print("文章相似度： %.2f" % similarity)
    # 将相似度结果写入指定文件
    f = open(path_3, 'w', encoding="utf-8")
    f.write(path_1[47:] + '  和  ' + path_2[47:] + '\n' + "文章相似度： %.2f" % similarity)
    f.close()



if __name__ == '__main__':
    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_add.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_1.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_del.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_2.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_1.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_3.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_10.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_4.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_15.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_5.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_add.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_add.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_6.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_add.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_1.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_7.txt')

    unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_1.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_15.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_8.txt')

unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig_0.8_dis_1.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\test_1.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_9.txt')

unit_test(r'D:\rjgc3119005411\3119005411\txt_test\test_txt\orig.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\test_2.txt',
              r'D:\rjgc3119005411\3119005411\txt_test\test_txt\result_10.txt')