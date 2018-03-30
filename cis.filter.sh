while read -a line
do

    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    awk '$3 == $6{print}' $line > $DIR/$RAWNAME.cis.txt &

done < $1
