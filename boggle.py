#! /usr/bin/env python
""""
Implementation of a Boggle cheater

Takes in a string of letters from the command line and 
returns the different different words that can be created
using those letters
"""

import itertools
import argparse

"""
Parses the arguments from the command line and calls the function boggle
"""
parser = argparse.ArgumentParser()
parser.add_argument("board", nargs = 1, help="a string of letters e.g. small")
args = parser.parse_args()
board = args.board[0]


"""
Imports words from a local dictionary into a python dictionary
"""
def create_dictionary(dictionary='/usr/share/dict/words'):
	with open(dictionary, 'r') as f:
		return {line.strip() for line in f.readlines()}

"""
Returns all permutations of length i of the letters
"""
def permutation(board, length):
	return set(itertools.permutations(board, length))
	 
"""
Prints all permutations that are availbale in the dictionary
"""
def boggle(board):
	words = create_dictionary()
	
	# Iterates through all possible lengths (words of length 2 - length of board)
	for i in xrange(2, len(board)+1):
		permutations = permutation(board, i)
		perm = []
		for p in permutations:	
			perm.append(''.join(elem[0] for elem in p)) # Joins letters into one string
		for item in (perm):
			if item.lower() in words:
				print item.lower()

boggle(board)

