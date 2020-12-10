
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day9Input.txt"
preamble = 25

if __name__ == "__main__":
    part1 = 0
    
    print("Advent of Code 2020 - Day 9")
    with open(inputfile, 'r') as f:
        data = [float(line.strip()) for line in f.readlines()]

    # Part 1
    for i in range(preamble,len(data)):
        foundit = 0
        for j in range(i-preamble,i):
            for k in range(j+1,i):
                if data[j] + data[k] == data[i]:
                    foundit = 1
                    break
        if not foundit:
            part1 = data[i]
            print("Part 1:", part1)
            break
            
     
    # Part 2
    for i in range(preamble,len(data)):
        for j in range(i-preamble,i):
            for k in range(j+1,i):
                running_total = data[j]
                while running_total + data[k] <= part1:
                    running_total += data[k]
                    k+=1
                j+=1
                if running_total == part1:
                    part2 = data[j-1] + data[k-2]
                    print("Part 2: ", part2)
                    exit()
                else:
                    running_total = 0
               
                