import re, sys


class illuminaSNPmanifest:

	
	def __init__( self, filepath):
		self.manifest={}

		f = open( filepath)
		body = f.read().split('[Assay]')
		lines=body[1].split('\n')

		for line in lines[2:]:
			cols=line.split(',')
			if len( cols ) < 20:
				continue

			probeID = cols[1]
			strand = cols[20]
			refAllele= cols[3].replace('[','').replace(']','').split('/')
			Chr = cols[9]
			pos = cols[10]
			ploidity = cols[11]


			self.manifest.setdefault( probeID,{ 'chr': Chr })
			self.manifest[ probeID ].setdefault('pos', pos )
			self.manifest[ probeID ].setdefault('allele', refAllele )
			self.manifest[ probeID ].setdefault('strand', strand )
			self.manifest[ probeID ].setdefault('ploidity',ploidity )
		


	def getProbeID( self ):
		return self.manifest.keys()

	def getStrand( self, key ):
		return self.manifest[key]['strand']
	

	def getChr( self, key ):
		return self.manifest[key]['chr']


	def getPos( self, key ):
		return self.manifest[key]['pos']

	
	def getPloidity( self, key ):
		return self.manifest[key]['ploidity']

	def getRefallele( self, key):
		return self.manifest[key]['allele']

