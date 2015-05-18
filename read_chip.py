from lib.illumina_chip_reader import *

chip= illuminaSNPChip('/data/genome_samples/omni_5_kcw_plus_strand.txt','rsid','5m') 

for key in chip.getKeys():
	print key, chip.getGenotype( key )

