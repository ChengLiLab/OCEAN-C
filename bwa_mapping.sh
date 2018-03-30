while read -a line
do
    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    mkdir -p "$DIR/BAM"
    echo "bowtie2 -p 8 --phred33 -x /lustre/user/liclab/publicData/reference/Homo_sapiens/UCSC/hg19/Sequence/Bowtie2Index/genome $line -S $DIR/BAM/$RAWNAME.trim.sam &"
done < $1

