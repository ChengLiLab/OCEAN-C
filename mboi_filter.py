#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import argparse
import sys
args=sys.argv
infilename=args[args.index('-i')+1]
outfilename=args[args.index('-o')+1]
genome = open('/lustre/user/liclab/jialm/resource/hg19.filter2.txt','r') # 24 条染色体序列信息，每条一行
reads = open(infilename,'r')
result = open(outfilename,'w')

data=[]
for chrom in genome:
        a = chrom.strip().upper()
        data.append(a) # 生成基因组信息的list列表

#reads信息： 1.read名，2正负链（0/1），3 chr(1~24), 4 起始位置        
for read in reads:
        n = int(read.split(' ')[3]) # n: read 起始位置
        
        if read.split(' ')[1] == '0': # read 在正链 
            f = data[int(read.split(' ')[2])-1][n:(n+536)] # all the alignment start location locates at the 5' of the positive chain
            if f.find('GATC') != -1:
                    result.write(read)
        else:
            f = data[int(read.split(' ')[2])-1][(n-500):n]
            if f.find('GATC') != -1:
                result.write(read)
result.close()
 
