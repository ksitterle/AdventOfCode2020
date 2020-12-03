
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day2Input.txt"

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 2")
    pt1_valid_password_count = 0
    pt2_valid_password_count = 0
    with open(inputfile) as f:
        for line in f.readlines():
            values = line.split()
            range = values[0].split('-')
            min = int(range[0])
            pos1 = min-1
            max = int(range[1])
            pos2 = max-1
            
            search_char = values[1].replace(':', "")            
            char_count = values[2].count(search_char)
               
            if char_count >= min and char_count <= max:
                pt1_valid_password_count += 1
                
            if (values[2][pos1] == search_char) != (values[2][pos2] == search_char) :
                pt2_valid_password_count += 1
                
                
print("Part 1:", pt1_valid_password_count)
print("Part 2:", pt2_valid_password_count)

