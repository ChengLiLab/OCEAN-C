# Hi-C data and OCEAN-C data processing

## Hi-C data and OCEAN-C data mapping and clearning
OCEAN-C reads were mapped and filtered as described in situ Hi-C data. The scripts are in Hic_analysis.tar.gz
Briefly, clean reads are first trimmed to 36 bp and then mapped to genome hg19 with bowtie2, and reads with MAPQ less than 1 are discarded. If the read pair locate in the same restriction fragment (MboI), they are defined as Dangling ends (inward), self-cycled (outward) or dumped pairs (same strand), and are all discarded. For the left read pairs that mapped to two different restriction fragments, if the distance between these two fragments is less than 1 kb, the read pair are discard due to their close distance in sequence. The left read pairs are considered valid and can be used to call peaks and generate interaction heatmaps. 

## HOCI detection 
The OCEAN-C peaks, which were defined as HOCIs. 
In U266 cell line, HOCIs were determined by ZINBA from the filtered data with the same parameters set for FAIRE-seq. 
In RPMI8226 and GM12878 cell lines, HOCIs were called by ZINBA with 'pscl' method from the filtered data for signals were too weak to be selected using the 'mixture' method.  Scripts are in Zinba_callpeak.tar.gz. 

