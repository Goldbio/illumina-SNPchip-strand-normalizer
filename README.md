# illumina SNP chip strand normalizer 

illumina's SNP chip produces both + and - stranded genotypes. 
For further analysis, this mixed stranded genotypes should be
normalized. 

This module transformes all - stranded genotypes into + stranded genotypes
based on each illumina SNP chip's manifest file. 



### Usage 

Print strandness of all probes in input SNP chip manifest file 

```python
	
from illumina_SNPchip_strand_normalizer import *

manifest = illuminaSNPmanifest( 'manifest file path' )

for probeID in manifest.getProbeID():
	print probeID, strand = manifest.getStrand( probeID )


```
