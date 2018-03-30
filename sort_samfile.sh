#!/bin/bash
while read -a line
do
BASE=`basename $line`
RAWNAME=${BASE%%.*}
DIR=`dirname $line`
echo "samtools sort  -m 2000000000  $line -o $DIR/$RAWNAME.trim.sort.bam &"
done < $1
