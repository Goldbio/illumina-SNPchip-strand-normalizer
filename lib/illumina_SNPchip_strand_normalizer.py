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
			refStrand = cols[20]
			refAllele= cols[3].replace('[','').replace(']','')
			Chr = cols[9]
			pos = cols[10]
			ploidity = cols[11]
			strand = cols[2]

			match=re.search( r'\[(.*)\]', cols[16] )
			if match:
				sourceAllele = match.group(1)
			else:
				continue


			self.manifest.setdefault( probeID,{ 'chr': Chr })
			self.manifest[ probeID ].setdefault('pos', pos )
			self.manifest[ probeID ].setdefault('refallele', refAllele )
			self.manifest[ probeID ].setdefault('refStrand', refStrand )
			self.manifest[ probeID ].setdefault('strand', strand )
			self.manifest[ probeID ].setdefault('ploidity',ploidity )
			self.manifest[ probeID ].setdefault('sourceAllele', sourceAllele )

		


	def getProbeID( self ):
		return self.manifest.keys()

	def getStrand( self, key ):
		return self.manifest[key]['strand']
	
	def getRefStrand( self, key):
		return self.manifest[key]['refStrand']
	
	def hasKey( self, key ):
		return key in self.manifest

	def getChr( self, key ):
		return self.manifest[key]['chr']


	def getPos( self, key ):
		return self.manifest[key]['pos']

	
	def getPloidity( self, key ):
		return self.manifest[key]['ploidity']

	def getRefallele( self, key):
		return self.manifest[key]['refallele']

	def getSourceAllele( self, key ):
		return self.manifest[key]['sourceAllele']

	def needTranscribe( self, key ):
		if self.manifest[key]['refallele'] == self.manifest[key]['sourceAllele'] and self.manifest[key]['refStrand'] == '-':
			return True
		elif self.manifest[key]['refallele'] != self.manifest[key]['sourceAllele'] and self.manifest[key]['refStrand'] == '+':
			return True
		else:
			return False
		



