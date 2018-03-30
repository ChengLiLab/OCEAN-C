import argparse
import sys
args=sys.argv
infilename=args[args.index('-i')+1]
outfilename=args[args.index('-o')+1]
reads = open(infilename,'r')
results = open(outfilename,'w')
for read in reads:
    if read.split(' ')[7] == "3":
        results.write(read)
    else:
        if read.split(' ')[7] == '1':
            if int(read.split(' ')[8]) > 1000:
                results.write(read)
        else:
            if int(read.split(' ')[8]) > 25000:
                results.write(read)
results.close()
