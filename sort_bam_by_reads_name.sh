while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    samtools sort  -m 6000000000 -n $line $DIR/$RAWNAME.trim.merge.unique.sort.rmd.namesorted.bam &
done < $1
