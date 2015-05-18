import sys, re
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
	




