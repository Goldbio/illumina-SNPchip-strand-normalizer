import sys, re , string


class illuminaSNPChip:

	def __init__( self, filepath , key_type, chip_name ):
		with open( filepath) as f:
		   self.name = chip_name
		   firstLine = f.readline()
		   if re.search( '\[Header\]', firstLine ):

					  '''
						  Macrogen illumina chip data formatted as below

							  [Head]
							  ...
							  [Data]
							  ...
					  '''

					  self.chip={}

					  self.isIllumina = True
					  data= f.read().split('[Data]')
					  data=data[1].split('\n')
					  for row in data[2:]:
						  snp= row.strip().split('\t')
						  if len( snp ) < 5 :
							  continue

						  probeID = snp[3]
						  match = re.search(r"rs\d+", snp[3] )
						  if match :
							  rsid=match.group(0)
						  else:
							  rsid=None

						  if key_type == 'chr-pos':
							  key = snp[1]+'-'+snp[2]	
						  elif key_type =='probe':
						     key = probeID
						  elif key_type == 'rsid':
							  if not rsid:
								  continue
							  else:
								  key = rsid


						  genotype = ''.join(  sorted( snp[4:6] ) )

						  	
						  	
						  self.chip.setdefault( key, { 'genotype': genotype })
						  self.chip[  key ].setdefault( 'rsid' ,  key  )
						  self.chip[  key ].setdefault( 'chr' , snp[1] )
						  self.chip[  key ].setdefault( 'pos' , snp[2] )
						  self.chip[  key ].setdefault( 'probeID' , probeID )


		   elif re.search( '23andMe', firstLine ):
				'''
					23andMe chip raw data file 
				'''
				self.chip={}
				for line in f:
					 if not re.search( '^#', line ):
						snp = line.split('\t')

						if re.search('[xy]', snp[1], re.IGNORECASE ):
							genotype=snp[3].strip()*2
						else:
							genotype=snp[3].strip()
							

						if key_type == 'chr_pos': 
							key = snp[1]+'-'+snp[2]
						elif key_type == 'rsid':
							key = snp[0]
							
						self.chip.setdefault( key, { 'genotype': ''.join( sorted( genotype) ) })
						self.chip[  key ].setdefault( 'rsid' ,  key  )
						self.chip[  key ].setdefault( 'chr' , snp[1] )
						self.chip[  key ].setdefault( 'pos' , snp[2] )



		   else:
				raise "Unknown SNP chip format"
			

	def isIlluminaChip( self ):
		return self.isIllumina
	
	def getSamplename( self):
		return self.name

	def getKeys( self ):
		return self.chip.keys()
	
	def getProbeID( self, key ):
		return self.chip[key]['probeID']

	def getChr( self, key ):
		return  self.chip[key]['chr'] 
	
	def getPos( self, key ):
		return self.chip[key]['pos']
	
	def getRSid( self, key ):
		if key in self.chip:
			return self.chip[key]['rsid']
		else:
			return False
	
	def getGenotype( self, key):
		return self.chip[key]['genotype']
	
	def getTranslatedGenotype( self, key ):
		return self.chip[key]['genotype'].translate( string.maketrans('ATGC','TACG'))

	
	def hasKey( self, key ):
		return key in self.chip
	
	def isValid(self, key):
		if re.search( '-',self.chip[key]['genotype']  ):
			return False
		else:
			return True 
	
	def isIndel(self, key ):
		if re.search( r'[ID]', self.chip[key]['genotype'] ):
			return True
		else:
			return False

	def isFWD(self, key ):
		
		return

	def getFWD_genotype( self, key ):
		
		return
	

