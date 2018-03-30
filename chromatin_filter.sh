while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    python ~/chromatin_filter.py -i $line -o $DIR/$RAWNAME.trim.unique.sort.rmd.namesorted.chromatin_filter.txt &

done < $1
