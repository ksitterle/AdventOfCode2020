
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day5Input.txt"

def do_search(direction, starting_range):
    final_range = []
    midpoint = int((starting_range[1]-starting_range[0])/2 + starting_range[0])
    if direction == 'F' or direction == 'L':
        final_range = [starting_range[0], midpoint]
    else:
        final_range = [midpoint+1, starting_range[1]]
    
    return final_range
        

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 5")
    seat_id = []
    with open(inputfile) as f:
        data = f.readlines()
                
    for line in data:
        next_range = [0, 127]
        next_col = [0,7]
        for i in range(0,7):
            next_range = do_search(line[i], next_range)
            
        for i in range(7,10):
            next_col = do_search(line[i], next_col)
        
        seat_id.append(next_range[0] * 8 + next_col[1])
       
    print("Max seat id:", max(seat_id))
    
    for i in range(min(seat_id),max(seat_id)):
        if seat_id.count(i) == 0:
            print("My seat:", i)
            exit()