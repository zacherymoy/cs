import re
import argparse
import sys
import os

# MATCH ANY PATTERN FROM FILE OR A DIRECTORY(S)
# RUN: python2 regargsFile.py MATCHWORD -f nameoffile.txt
# RUN: python2 regargsFile.py MATCHWORD -d nameofdirectory

def file_cruncher(fname, word):
	with open(fname)as searchFile:
		lineNum = 0
		for line in searchFile.readlines():
			line = line.strip('\n\r')
			lineNum += 1
			searchResult = re.search(word, line, re.M|re.I)
			if searchResult:
				# SLICING THE PATH(OPTIONAL)
				xx = fname.split('/')
				yy = (xx[-2] +'/'+ xx[-1])
				zz = ''.join(yy)
				print('\033[1;35m{}\033[1;m {}: {}'.format(zz, str(lineNum), line))

# PASS DIRECTORIES FILENAMES INTO A LIST
dir_file_list = []

def dir_contents(parent):
	for child in os.listdir(parent):
		fname = os.path.join(parent, child)
		if os.path.isdir(fname):
			dir_contents(fname)	
		else:
			dir_file_list.append(fname)

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument('word', help='Specify word to search')
	parser.add_argument('-f', '--fname', help='Need a filename')
	parser.add_argument('-d', '--dirpath', help='search directory(s)')

	if len(sys.argv[1:]) == 0:
		print('')
		print('TO RUN: python2 regargsFile.py <WORD> <[-f|-d]> <[FILENAME|DIRECTORY]>')
		print('')
		parser.print_help()
		parser.exit()

	args = parser.parse_args()
	fname = args.fname
	word = args.word

	try:
		if args.dirpath: #PASS A DIRECTORY
			dir_contents(args.dirpath)

			for listed_file in dir_file_list:
				file_cruncher(listed_file, word)
		else: #OR PASS A FILE
			file_cruncher(fname, word)

	except FileNotFoundError:print('No such file or directory')
	except IsADirectoryError:print('Is a directory')
	except NotADirectoryError:print('Not a directory')
	except UnicodeDecodeError:print('Unicode Decode Error :-(') #PYTHON 3


if __name__ == '__main__':
	Main()