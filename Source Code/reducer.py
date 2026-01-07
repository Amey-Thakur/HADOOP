"""
=========================================================================================
Project Name    : HADOOP - Matrix Multiplication (MapReduce)
Description     : Reducer script for aggregating intermediate key-value pairs to 
                  compute the final dot product for each cell in the result matrix.
Author          : Amey Thakur
GitHub Profile  : https://github.com/Amey-Thakur
Repository Link : https://github.com/Amey-Thakur/HADOOP
Date            : October 6, 2021
=========================================================================================
"""

#!/usr/bin/env python

import sys
from operator import itemgetter

# Initialization: Track indices and aggregate values (Step 1: Setup)
prev_index = None
value_list = []

# Process incoming key-value pairs from standard input (Step 2: Reduce Operation)
for line in sys.stdin:
    # Expected format: (row, col) \t common_index \t value
    curr_index, index, value = line.rstrip().split("\t")
    index, value = map(int, [index, value])
    
    if curr_index == prev_index:
        # Batch values belonging to the same (row, col) cell
        value_list.append((index, value))
    else:
        # New cell index detected; compute result for the previous cell
        if prev_index:
            # Sort by common index to align elements for dot product
            value_list = sorted(value_list, key=itemgetter(0))
            i = 0
            result = 0
            # Compute dot product: sum(A[i,k] * B[k,j])
            while i < len(value_list) - 1:
                if value_list[i][0] == value_list[i + 1][0]:
                    result += value_list[i][1] * value_list[i + 1][1]
                    i += 2
                else:
                    i += 1
            # Output final computed value: row, col, result
            print("%s,%s" % (prev_index, str(result)))
        
        # Reset trackers for the current cell index
        prev_index = curr_index
        value_list = [(index, value)]

# Final block: Process the last batch of values (Step 3: Cleanup)
if curr_index == prev_index:
    value_list = sorted(value_list, key=itemgetter(0))
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1] * value_list[i + 1][1]
            i += 2
        else:
            i += 1
    print("%s,%s" % (prev_index, str(result)))