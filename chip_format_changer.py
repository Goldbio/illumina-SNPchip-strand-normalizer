import sys, re


f = open( sys.argv[1] )

for line in f.readlines():
	cols = line.split('\t')
	if len( cols ) < 7:
		print line.strip()
	else:
		linePrint=[  cols[0], cols[2], cols[3], cols[1], cols[12], cols[13] ] #12, 13
		print '\t'.join( linePrint )



