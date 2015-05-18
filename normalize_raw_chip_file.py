import sys, re
from lib.illumina_SNPchip_strand_normalizer import *
from lib.illumina_chip_reader import *

def normalizeRawChipFile( chipFilePath, manifest ):
	
	f = open( chipFilePath )

	for line in f.read().splitlines():
		cols = line.split('\t')
		if len( cols) < 7 or not manifest.hasKey( cols[3] ) :
			print line

		else:
			if manifest.needTranscribe( cols[3] ) : 
				cols[4] = cols[4].translate( string.maketrans('ATGC','TACG'))
				cols[5] = cols[5].translate( string.maketrans('ATGC','TACG'))

			print '\t'.join( cols )




manifest=illuminaSNPmanifest( sys.argv[2])
normalizeRawChipFile( sys.argv[1], manifest)
