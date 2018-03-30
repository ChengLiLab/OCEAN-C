#!/usr/bin/python
# _*_ coding: UTF-8 _*_
# 此脚本将经过chromatin, restriction site 过滤之后的read1, read2 写成一行：
import argparse
import sys
args=sys.argv
infilename=args[args.index('-i')+1]
outfilename=args[args.index('-o')+1]
samfile = open(infilename,'r')
result = open(outfilename,'w')
delimiter = '\t'

a = samfile.readline() # 读进第一行

for line in samfile:

    if line.split('\t')[0] == a.split('\t')[0]:
      # 将名字相同个的两个read写成一行：
        result.write(a.strip() +'\t'+ delimiter.join(line.split('\t')[1:4]))
    else: a = line
result.close()
