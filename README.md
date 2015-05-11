# illumina SNP chip strand normalizer 

illumina's SNP chip produces both + and - stranded genotypes. 
For further analysis, this mixed stranded genotypes should be
normalized. 

This module transformes all - stranded genotypes into + stranded genotypes
based on each illumina SNP chip's manifest file. 



### Exam usage 

If you want to print out strandness of all probes in SNP chips, first download manifest file for SNP chips of your interest from http://support.illumina.com/array/downloads.html. Download Manifest file(CSV format) under 'Product files' section of the SNP chip of your interest.

When you prepare manifest file, use this library to print out strandness of all probes as exam codes below. 

```python
	
from illumina_SNPchip_strand_normalizer import *

manifest = illuminaSNPmanifest( 'manifest file path' )

for probeID in manifest.getProbeID():
	print probeID, strand = manifest.getStrand( probeID )


```
