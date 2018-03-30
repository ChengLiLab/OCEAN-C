while read -a line
do
BASE=`basename $line`
RAWNAME=${BASE%%.*}
DIR=`dirname $line`
echo "samtools view -bq 1 $line > $DIR/$RAWNAME.trim.merge.unique.bam &"
done < $1
