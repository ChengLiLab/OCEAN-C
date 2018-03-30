while read -a line

do

  BASE=`basename $line`
  RAWNAME=${BASE%%.*}
  DIR=`dirname $line`
  python /lustre/user/liclab/jialm/CODE/mboi_filter.py -i $line -o $DIR/$RAWNAME.trim.merge.unique.sort.rmd.namesorted.chromatin_filter.mboifilter.txt &

done < $1
