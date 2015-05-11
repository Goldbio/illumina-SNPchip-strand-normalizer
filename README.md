# illumina SNP chip strand normalizer 

illumina's SNP chip produces both + and - stranded genotypes. 
For further analysis, this mixed stranded genotypes should be
normalized. 

This module transformes all - stranded genotypes into + stranded genotypes
based on each illumina SNP chip's manifest file. 



### Exam usage 

If you want to print out strandness of all probes in SNP chips, first download manifest file for SNP chips of your interest from http://support.illumina.com/array/downloads.html. Download Manifest file(CSV format) under 'Product files' section of the SNP chip of your interest.

1. Print out strandness of all probes as exam codes below. 

```python
	
from illumina_SNPchip_strand_normalizer import *

manifest = illuminaSNPmanifest( 'manifest file path' )

for probeID in manifest.getProbeID():
	print probeID, strand = manifest.getStrand( probeID )


```


2. To translate '-' stranded genotypes to '+' stranded genotypes

```python

from lib.illumina_SNPchip_strand_normalizer import *
from lib.illumina_chip_reader import *

chip = illuminaSNPChip( sys.argv[1], 'probe','omni5' ) 
manifest=illuminaSNPmanifest( sys.argv[2])


for probe in chip.getKeys():
   genotype = chip.getGenotype( probe )
   transGeno = genotype
   strand= manifest.getStrand( probe )

   if strand == '-':
      transGeno = chip.getTranslatedGenotype( probe )

   linePrint=[ probe, chip.getChr(probe), chip.getPos( probe), genotype, strand, transGeno ]
	print ','.join( linePrint )



```
