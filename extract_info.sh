while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    samtools view $line | awk '{print $1"\t"$2"\t"$3"\t"$4}' > $DIR/$RAWNAME.trim.merge.unique.sort.rmd.namesorted.sam &

done < $1
