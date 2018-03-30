
while read -a line 
do
    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    echo "fastx_trimmer  -Q33  -l 36 -i $line -o $DIR/$RAWNAME.trim.fq &"
done < $1 
