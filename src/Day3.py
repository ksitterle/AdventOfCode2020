
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day3Input.txt"

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 3")
    final_value = 1
    with open(inputfile) as f:
        data = f.readlines()
    
    directions = [1,1], [3,1], [5,1], [7,1], [1,2]
    
    for right, down in directions:
        current_pos = 0
        tree_count = 0        
            
        for i in range(0, len(data), down):
            line = data[i].rstrip()
            if line[current_pos % len(line)] == '#':
                tree_count += 1
            current_pos += right  
            
        print("Part 1:", tree_count)
        final_value *= tree_count
                
    print("\nPart 2:", final_value)

