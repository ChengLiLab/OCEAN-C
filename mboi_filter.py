#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import argparse
import sys
args=sys.argv
infilename=args[args.index('-i')+1]
outfilename=args[args.index('-o')+1]
genome = open('~/hg19.filter2.txt','r') # sequences of 24 chromosomes, each a line 
reads = open(infilename,'r')
result = open(outfilename,'w')

data=[]
for chrom in genome:
        a = chrom.strip().upper()
        data.append(a) 

#reads info： 1.read name，2.strand，3 chr(1~24), 4 start sites        
for read in reads:
        n = int(read.split(' ')[3]) # n: read start sites
        
        if read.split(' ')[1] == '0': # strand + 
            f = data[int(read.split(' ')[2])-1][n:(n+536)] # all the alignment start location locates at the 5' of the positive chain
            if f.find('GATC') != -1:
                    result.write(read)
        else:
            f = data[int(read.split(' ')[2])-1][(n-500):n]
            if f.find('GATC') != -1:
                result.write(read)
result.close()
 
