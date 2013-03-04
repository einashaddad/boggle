#! /usr/bin/env python
""""
Implementation of a Boggle cheater

Takes in a string of letters from the command line and 
returns the different words that can be created
using those letters
"""

import itertools
import sys
import boggle_graph

"""
Parses the arguments from the command line
"""
letters = sys.argv[1]
n = int(sys.argv[2])
if len(sys.argv) == 4:
    dictionary_path = sys.argv[3]
else:
    dictionary_path = '/usr/share/dict/words'

def create_dictionary(dictionary = dictionary_path):
    """
    Imports words from a local dictionary into a python set
    """
    try:
        with open(dictionary, 'r') as f:
            return {line.strip().lower() for line in f.readlines()}
    except IOError:
        print "No dictionary at /usr/share/dict/words. Please enter path to dictionary at command line." 
        sys.exit()

def dfs(visited_nodes, graph, node=('', (None, None))):
    """
    Returns words of length 3 or more on the board that are present in the dictionary
    """    
    global dictionary
    visited_nodes = visited_nodes + [node]

    word_fragment = "".join([letter for letter, position in visited_nodes])

    if len(word_fragment) >= 3 and word_fragment in dictionary:
        yield word_fragment

    good_neighbors = [n for n in graph[node] if n not in visited_nodes]

    for neighbor in good_neighbors:
        for result in dfs(visited_nodes, graph, neighbor):
            yield result

if __name__ == "__main__":
    dictionary = create_dictionary()
    print "dictionary created"

    board, position = boggle_graph.make_board(letters, n)
    graph = boggle_graph.make_graph(board, position)
    words_out = []
    for word in dfs([], graph):
        words_out.append(word)

    print words_out
    print len(words_out)