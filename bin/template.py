#!/usr/bin/env python3

# Script that makes an input file with the specified parameters

import argparse
import importlib

parser = argparse.ArgumentParser(description='Get the geometry of an output file.')
parser.add_argument('-p', '--program', help='The program', type=str, default='orca')
parser.add_argument('-g', '--geom', help='The geometry file', type=str, default='geom.yxz')
parser.add_argument('-n', '--nprocs', help='The number of processors to use', type=int, default=8)
parser.add_argument('-j', '--jobtype', help='The jobtype to run', type=str, default='Opt')
parser.add_argument('-f', '--functional', help='The functional to use', type=str, default='B3LYP')
parser.add_argument('-b', '--basis', help='The basis set to use', type=str, default='sto-3g')
parser.add_argument('-i', '--iterations', help='The maximum number of SCF iterations', type=int, default=300)

args = parser.parse_args()

geom = ''
try:
    with open('geom.xyz', 'r') as f:
        geom = f.read().strip()
except IOError:
    print("No geometry specified")

program = args.program
if program:
    try:
        mod = importlib.import_module('qgrep.' + program)
        if hasattr(mod, 'template'):
            temp = mod.template(geom, args.nprocs, args.jobtype, args.functional, args.basis, args.iterations)
        else:
            print(program + ' does not yet have template implemented.')
    except ImportError:
        print(program + ' is not yet supported.')
else:
    print('Cannot determine what program made this output file.')

with open('input.dat', 'w') as f:
    f.write(temp)
