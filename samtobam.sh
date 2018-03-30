while read -a line
do
BASE=`basename $line`
RAWNAME=${BASE%%.*}
DIR=`dirname $line`
echo "samtools view -bS -h $line > $DIR/$RAWNAME.trim.bam &"
done < $1
