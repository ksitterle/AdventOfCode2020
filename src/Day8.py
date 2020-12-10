
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day8Input.txt"
code = []
lastpc = 74

# Set to 1 to run part 1
part1 = 1

def dotest(i):
    pc, accumulator, done = 0, 0, 0
    history = []
    while(not done):
        if pc in history:
            done = 1
            if part1:
                print("Part 1 Accumulator: ", accumulator)
            return 0
        history.append(pc)
        if pc == len(code):
            print("Part 2 Accumulator:", accumulator)
            return 1
        if code[pc][0] == "nop":
            pc += 1
        elif code[pc][0] == "acc":
            accumulator += int(code[pc][1])
            pc += 1
        else:
            pc += int(code[pc][1])
            
if __name__ == "__main__":
    print("Advent of Code 2020 - Day 8")
    with open(inputfile, 'r') as f:
        code = [line.split() for line in f.readlines()]

    # Part 1
    part1 = 1
    dotest(0)
    part1 = 0                

    # Part 2
    # Modify each nop and jmp instruction and test
    for i in range(0, len(code)):
        if code[i][0] == "nop":
            code[i][0] = "jmp"
            dotest(i)
            code[i][0] = "nop"                
        elif code[i][0] == "jmp":
            code[i][0] = "nop"
            dotest(i)
            code[i][0] = "jmp"
