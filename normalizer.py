import sys, re
from lib.illumina_SNPchip_strand_normalizer import *


manifest=illuminaSNPmanifest( sys.argv[1])

# Print out some features of each probe in manifest file 

for key in manifest.getProbeID():
	print manifest.getChr(key), manifest.getPos( key ), manifest.getStrand(key), manifest.getRefallele( key),  manifest.getSourceAllele(key), manifest.needTranscribe( key)





