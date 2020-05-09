#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

def main():
    with open('cmn.txt','rt') as f1:
        f11 = f1.readlines()#将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
    f2 = open('re.txt','w')#打开一个文件，用于写入，后面的'wb'表示每次写入前格式化文本，如果此文件不存在，则创建一个此文件名的文件

    for x in f11:#以行为单位遍历读入的内容
        x1=x.split('\t')[0] #文本分割，以table键分割
        x2=x.split('\t')[1]
        f2.write(x1+'\t'+x2+'\n')
    f2.close()#执行完毕关闭文件
    print('end')


if __name__ == '__main__':
    main()
