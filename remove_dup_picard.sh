while read -a line
do
BASE=`basename $line`
RAWNAME=${BASE%%.*}
DIR=`dirname $line`
echo "java -Xms2g -Xmx8g -XX:ParallelGCThreads=8 -jar /home/menghw/software/picard-tools-1.140/picard.jar MarkDuplicates INPUT=$line OUTPUT=$DIR/$RAWNAME.trim.merge.unique.sort.rmd.bam METRICS_FILE=$DIR/$RAWNAME.trim.merge.unique.rmd.sort.bam.metrics ASSUME_SORTED=true REMOVE_DUPLICATES=true > $DIR/$RAWNAME.trim.merge.unique.sort.rmd.log &"
done < $1



#java -Xms2g -Xmx8g -XX:ParallelGCThreads=8 -jar /home/menghw/software/picard-tools-1.140/picard.jar MarkDuplicates INPUT=./tmp.data/BAM/Hela-nucleolus-genomeseq.bam   OUTPUT=/tmp.data/BAM/Hela-nucleolus-genomeseq_rmdup.bam METRICS_FILE=./tmp.data/BAM/Hela-nucleolus-genomeseq_picard.matrix  ASSUME_SORTED=true REMOVE_DUPLICATES=true > ./tmp.data/BAM/Hela-nucleolus-genomeseq_rmdup.log  &
