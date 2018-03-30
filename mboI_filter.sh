while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    python ~/mboi_filter.py -i $line -o $DIR/$RAWNAME.trim.unique.sort.rmd.namesorted.chromatin_filter.mboi_filter.txt &

done < $1


