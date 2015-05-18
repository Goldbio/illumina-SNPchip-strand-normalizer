import sys, re
from lib.illumina_SNPchip_strand_normalizer import *
from lib.illumina_chip_reader import *

def normalizeRawChipFile( chipFilePath, manifest ):
	
	total=0
	count=0

	f = open( chipFilePath )
	
	for line in f.read().splitlines():
		cols = line.split('\t')
		if len( cols) < 7 or not manifest.hasKey( cols[3] ) :
			print line

		else:
			probeID = cols[3]
			genotype = cols[4:6]

			genoSource=manifest.getSourceAllele( probeID ).split('/')
			#print probeID, cols[4:6],manifest.getStrand( probeID) ,manifest.getRefallele( probeID ), manifest.getSourceAllele( probeID ) , manifest.getRefStrand(probeID)

			### count ###
			total+=1
			genoIn=0
			for g in genotype:
				if g in genoSource:
					genoIn +=1


			if genoIn == 2:
				count+=1
			else :
				print probeID, cols[4:6],manifest.getStrand( probeID) ,manifest.getRefallele( probeID ), manifest.getSourceAllele( probeID ) , manifest.getRefStrand(probeID)
				
				
	
	print count, total 




manifest=illuminaSNPmanifest( sys.argv[2])
normalizeRawChipFile( sys.argv[1], manifest)
