import sys, re
from lib.illumina_SNPchip_strand_normalizer import *


manifest=illuminaSNPmanifest( sys.argv[1])

# Print strandness of all probes in SNP chip
for key in manifest.getProbeID():
	print manifest.getChr(key), manifest.getPos( key ), manifest.getStrand(key)





