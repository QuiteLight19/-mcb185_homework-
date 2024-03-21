#91 translate by Aman Panigrahi
#Co-Authors: Aman, Ashley

import argparse
import mcb185
import biofun

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
	help='min protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='examines anti-parallel strand')
arg = parser.parse_args()

def print_row(seq):
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])

for defline, seq in mcb185.read_fasta(arg.file):
	trans = biofun.translate(seq[seq.find('ATG'):])
	if '*' in trans and trans.find('*') + 1 >= arg.min:
		print(f'{defline}')
		print_row(trans[:trans.find('*')])
	if arg.anti:
		anti = biofun.revcomp(seq)
		if 'ATG' in anti:
			revanti = biofun.translate(anti[anti.find('ATG'):])
			if '*' in revanti and revanti.find('*') + 1 >= arg.min:
				print(f'{defline} anti')
				print_row(revanti[:revanti('*')])