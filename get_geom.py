#!/usr/bin/python

# Script that takes an output file and gets the last geometry

import argparse
from helper import read

parser = argparse.ArgumentParser( description='Get the geometry of an output file.' )
parser.add_argument( '-i', '--input', help='The file to be read.', type=str, default='output.dat' )
parser.add_argument( '-o', '--output', help='Where to output the geometry.', type=str, default='geom.xyz' )
parser.add_argument( '-t', '--type', help='The geometry style', type=str, default='xyz' )
parser.add_argument( '-u', '--units', help='What units to output the geometry in.', type=str, default='angstrom' )

args = parser.parse_args()

lines, program = read( args.input )

geom = ''
if program == 'orca':
	import orca
	geom = orca.get_geom( lines, args.type, args.units )
elif program == 'qchem':
	import qchem
	geom = qchem.get_geom( lines )
elif program == 'psi4':
	import psi4
	geom = psi4.get_geom( lines )
else:
	print "Not yet supported"

if not args.output == '':
	out = ''
	for line in geom:
		out += '\t'.join( line.split() ) + '\n'

	with open( args.output, 'w' ) as f:
		f.write( out )
