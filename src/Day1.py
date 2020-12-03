
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input\Day1Input.txt"

def main():
    return 0

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 1 Part 1")
    
    with open(inputfile) as f:
        values = [int(line.strip()) for line in f.read().splitlines()]
    
    # Find the values that sum to 2020
    for num1 in values:
        for num2 in values:
            for num3 in values:
                sum = num1 + num2 + num3
                if sum == 2020:
                    print("found them! ", num1, " ", num2, " ", num3)
                    print("answer is ", num1 * num2 * num3)
                    exit()
    
