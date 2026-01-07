"""
=========================================================================================
Project Name    : HADOOP - Matrix Multiplication (MapReduce)
Description     : Mapper script for partitioning Matrix A and Matrix B elements into 
                  intermediate key-value pairs suitable for multiplication and reduction.
Author          : Amey Thakur
GitHub Profile  : https://github.com/Amey-Thakur
Repository Link : https://github.com/Amey-Thakur/HADOOP
Date            : October 6, 2021
=========================================================================================
"""

#!/usr/bin/env python

import sys

# Load matrix dimensions from cache file (Step 1: Configuration)
# cache.txt contains (row_a, col_b) to determine the output key space
try:
    cache_info = open("cache.txt").readlines()[0].split(",")
    row_a, col_b = map(int, cache_info)
except IndexError:
    # Error handling for empty or malformed cache files
    sys.exit(1)
 
# Process incoming matrix elements from standard input (Step 2: Map Operation)
for line in sys.stdin:
  # Expected format: matrix_id, row, col, value
  matrix_index, row, col, value = line.rstrip().split(",")
  
  if matrix_index == "A":
    # For Matrix A (row i, col k): Emit ((i, j), k, A[i,k]) for all j in Col(B)
    for i in range(0,col_b):
      key = row + "," + str(i)
      # Emit intermediate pair: ((target_row, target_col), common_index, value)
      print("%s\t%s\t%s"%(key,col,value))
  else:
    # For Matrix B (row k, col j): Emit ((i, j), k, B[k,j]) for all i in Row(A)
    for j in range(0,row_a):
      key = str(j) + "," + col 
      # Emit intermediate pair: ((target_row, target_col), common_index, value)
      print ("%s\t%s\t%s"%(key,row,value))