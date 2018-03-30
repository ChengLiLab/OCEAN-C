import argparse
import sys
args=sys.argv
infilename=args[args.index('-i')+1]
outfilename=args[args.index('-o')+1]
reads = open(infilename,'r')
results = open(outfilename,'w')


genome = open('~/hg19.filter2.txt','r')
data=[]
for chrom in genome:
        tmp = chrom.strip().upper()
        data.append(tmp)


for read in reads:
	n1 = int(read.split('\t')[3])
	n2 = int(read.split('\t')[6])
	b  = n1 - n2
	chrnum = int(read.split('\t')[2])-1
	if int(read.split('\t')[1]) == int(read.split('\t')[4]):
                if b >0:
                        f1 = (data[chrnum][(n1-50000):n1])[::-1]
                        f2 = data[chrnum][n2:(n2+50000)]
                        f1num = f1.find('CTAG')+3
                        f2num = f2.find('GATC')+3
                        results.write(read.strip()+' 3 '+str(abs(b)-f1num-f2num)+'\n')
                else:
                        f1 = (data[chrnum][(n2-50000):n2])[::-1]
                        f2 = data[chrnum][n1:(n1+50000)]
                        f1num = f1.find('CTAG')+3
                        f2num = f2.find('GATC')+3
                        results.write(read.strip()+' 3 '+str(abs(b)-f1num-f2num)+'\n')
	else:
			if read.split('\t')[1] == '16' and read.split('\t')[4] == '0':
				if b >0:
                                        f1 = (data[chrnum][(n1-50000):n1])[::-1]
                                        f2 = data[chrnum][n2:(n2+50000)]
                                        f1num = f1.find('CTAG')+3
                                        f2num = f2.find('GATC')+3
                                        results.write(read.strip()+' 1 '+str(abs(b)-f1num-f2num)+'\n')
				else:
                                        f1 = (data[chrnum][(n2-50000):n2])[::-1]
                                        f2 = data[chrnum][n1:(n1+50000)]
                                        f1num = f1.find('CTAG')+3
                                        f2num = f2.find('GATC')+3
                                        results.write(read.strip()+' 2 '+str(abs(b)-f1num-f2num)+'\n')
			else:
				if b >0:
                                        f1 = (data[chrnum][(n1-50000):n1])[::-1]
                                        f2 = data[chrnum][n2:(n2+50000)]
                                        f1num = f1.find('CTAG')+3
                                        f2num = f2.find('GATC')+3
                                        results.write(read.strip()+' 2 '+str(abs(b)-f1num-f2num)+'\n')
				else:
                                        f1 = (data[chrnum][(n2-50000):n2])[::-1]
                                        f2 = data[chrnum][n1:(n1+50000)]
                                        f1num = f1.find('CTAG')+3
                                        f2num = f2.find('GATC')+3
                                        results.write(read.strip()+' 1 '+str(abs(b)-f1num-f2num)+'\n')
