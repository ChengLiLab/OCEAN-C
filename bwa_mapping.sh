while read -a line
do
    BASE=`basename $line`
    RAWNAME=${BASE%%.*}
    DIR=`dirname $line`
    mkdir -p "$DIR/BAM"
    echo "bowtie2 -p 8 --phred33 -x ~/user/Bowtie2Index/genome $line -S $DIR/BAM/$RAWNAME.trim.sam &"
done < $1

