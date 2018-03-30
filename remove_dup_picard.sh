while read -a line
do
BASE=`basename $line`
RAWNAME=${BASE%%.*}
DIR=`dirname $line`
echo "java -Xms2g -Xmx8g -XX:ParallelGCThreads=8 -jar ~/picard-tools-1.140/picard.jar MarkDuplicates INPUT=$line OUTPUT=$DIR/$RAWNAME.trim.merge.unique.sort.rmd.bam METRICS_FILE=$DIR/$RAWNAME.trim.merge.unique.rmd.sort.bam.metrics ASSUME_SORTED=true REMOVE_DUPLICATES=true > $DIR/$RAWNAME.trim.merge.unique.sort.rmd.log &"
done < $1

