# Hi-C /OCEAN-C pipline:
## before data processing, put all fastq file in a new folder

01) All fastq file names were written in input.file.01:
    ls *.fastq > input.file.01

02) All reads were trimmed to 36 bp before mapping: 
    sh trim_reads.sh input.file.01
    
03) Names of all trimmed fastq files were written in input.file.02:
    ls *.trim.fq > input.file.02

04) All trimmed fastq files were mapped to human genome (hg19) with Bowtie2: 
    sh bowtie2_mapping.sh input.file.02 
    
05) Names of all mapped .sam files were written in input.file.03: 
    ls *.sam > input.file.03

06) All mapped sam files were transfered to bam formate: 
    sh samtobam.sh input.file.03
    
07) Names of all bam files were then written into input.file.04:
    ls *.bam > input.file.04

08) All bam files were sorted: 
    sh sort_samfile.sh input.file.04
    
09) Names of all sorted bam files were written into input.file.05: 
    ls *.trim.sort.bam > input.file.05
    
10) All unique mapped reads were selected: 
    sh unique_filter_bam.sh input.file.05 
       
11) Names of all unique mapped files were written into input.file.06: 
    ls *.trim.unique.bam > input.file.06
    
12) All unique mapped reads were then remove duplicates with picard: 
    sh remove_dup_picard.sh input.file.06 
    
13) Names of all dup-removed files were written into input.file.07: 
    ls *.rmd.bam > input.file.07

14) All dup-removed reads were then sorted by readnames: 
    sh sort_bam_by_reads_name.sh input.file.07
   
15) Names of all name-sorted files were written into input.file.08: 
    ls *.namesorted.bam > input.file.08
   
16) All name-sorted bam files were transfered into sam formate, and the first four columns were extracted: 
    sh extract_info.sh input.file.08
   
17) Names of all extracted files were written into input.file.09: 
    ls *.rmd.namesorted.sam > input.file.09
 
18) All reads mapped to the 1-24 chromosomes were selected, and names of the reasult files were written into input.file.10: 
    sh chromatin_filter.sh input.file.09,
    ls *.chromatin_filter.txt > input.file.10
    
19) The reads 500bp away from restriction enzyme cutting sites (MboI) were then removed: 
    sh mboI_filter.sh input.file.10
    
20) Names of all these mboi filtered files were written into input.file.11, and read pairs with the same readnames were then merged into one line:
    ls *..mboi_filter.txt > input.file.11
    sh chromatin_filter_mboI_merge.sh input.file.11
    
21) Reads were then performing fragment filter:
    a) First, read pairs mapped to the same chromosome are selected as the cis-interacting reads: 
       awk '$3 == $6{print}' ~/*.mboi_filter.merge.txt > ~/cis.txt
    
    b) Second, add two columns of info into the cis.txt: 
      python ~/strandori_gapsize.py > cis.add.gapsize
      
    c) Third, the read pairs in the same fragment were removed:
      less ~/cis.add.gapsize |awk '{if($9>=0){print}}' > ~/cis.add.gapsize.nosamfrag.txt
      
    d) Finally, read pairs were filtered accroading to the length:
      python fragement_level_filter.py > cis_fragment_filtered.txt 



# The cis_fragment_filtered.txt files from Hi-C and OCEAN-C were used to call HOCIs:

1)Rscript Zinba_mixture_call.peak.r #('mixture' method)

2)Rscript Zinba_pscl_call.peak.r #('pscl' method)
