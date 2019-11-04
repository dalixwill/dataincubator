#!/usr/bin/env python

"""
Consider a grid in d-dimensional space. There are n grid lines in each 
dimension, spaced one unit apart. We will consider a walk of m steps from grid 
intersection to grid intersection. Each step will be a single unit movement in 
any one of the dimensions, such that it stays on the grid. We wish to look at 
the number of possible paths from a particular starting location on this grid.

"""
import sys
import numpy as np
from itertools import product

def traverse_nodes(neighbor_list, start, length, paths, 
                      path=[], showPath=False):
    path = path + [start]
    
    if len(path) == length+1:
        if showPath:
            print(path)
        paths.append(path)
    else:
        for node in neighbor_list[str(start)]:
            traverse_nodes(neighbor_list, node, length, paths, path, showPath)

def compute_paths(nDims, nGridLines, nMoves, start, showPath=False):
        
    # Generate node list 
    nodes = [node for node in product(range(0, nGridLines), repeat=nDims)]
    nodes = np.asarray(nodes)
    
    # Calculate the distances to each nearest neighbor, dnn
    dnn = []
    for inode, anode in enumerate(nodes):
        dnn.append(np.linalg.norm(np.asarray(anode)-np.asarray(nodes), axis=1))
    dnn = np.asarray(dnn)
    
    # Create a boolean mask where true values are valid neighbors
    isnn = np.zeros(dnn.shape, dtype=bool)
    isnn[dnn==1] = True
    
    # Create nearest neighbor dictionary nn, where each key-value 
    # pair is a node and its respective neighbors
    nn = {}
    for irow, row in enumerate(isnn):
        nn[str(nodes[irow])] = nodes[row]

    paths = []
    traverse_nodes(nn, start, nMoves, paths, path=[], showPath=showPath)
    
    print("When the dimension d = {},".format(nDims))
    print("the number of grid lines n = {},".format(nGridLines))
    print("the number of allowed moves m = {},".format(nMoves))
    outtext = "and the starting position is " + str(start)
    print(outtext)
    print("There are {} possible moves.".format(len(paths)))
    
    return paths

def main():
  
  if len(sys.argv) < 5:
    print("\nPlease run command as follows:\n")
    print("\tpython nodeConnection.py <dim> <grid lines> <steps> <start>")
    print("\twhere <dim>, <grid lines> and <steps> are integers,")
    print("\tand <start> is a string of form '[x0 x1 ... xd]' with integer")
    print("\tvalues x0...xd for the starting point of each dimension.\n")
  else:
    start = np.asarray(sys.argv[4])
    m = int(sys.argv[3])
    n = int(sys.argv[2])
    d = int(sys.argv[1])

    compute_paths(d, n, m, start)

if __name__ == '__main__' : main()
