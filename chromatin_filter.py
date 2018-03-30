#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import argparse
import sys
args=sys.argv
infilename=args[args.index('-i')+1]
outfilename=args[args.index('-o')+1]
samfile = open(infilename,'r')
result = open(outfilename,'w')
#delimiter = ' '
delimiter = ' '
for line in samfile:
    if 'Un_g' not in line:
        if 'hap'  not in line:
            if 'random' not in line:
                if 'chrM' not in line:
                    line = line.replace('chr','')# remove 'chr'
                    line = line.replace('X','23')# x chromatin transfer to '23'
                    line = line.replace('Y','24')# y chromatin transfer to '24'
                    if line.split(' ')[1] =='0': # 0：mapped to '+' strand
                        result.write(line)
                    else:
                        result.write(line.split(' ')[0]+' 1 '+ delimiter.join(line.split(' ')[2:4])) # 1， mapped to '-' strand
result.close()
