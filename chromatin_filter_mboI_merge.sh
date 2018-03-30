while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    python ~/reads_merge.py  -i $line -o $DIR/$RAWNAME.chromatin_filter.mboifilter.merge.txt &

done < $1
