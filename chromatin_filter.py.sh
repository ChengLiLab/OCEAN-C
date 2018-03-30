while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    python /lustre/user/liclab/jialm/CODE/chromatin_filter.py -i $line -o $DIR/$RAWNAME.trim.merge.unique.sort.rmd.namesorted.chromatin_filter.txt &

done < $1
