#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
inputfile = "input/Day11Input.txt"
seats = []
new_seats = []
numrows = 0
numcols = 0

def getpart2(row,col):
    adj = 0
    for i in range(-1,2):        
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            m = row+i
            n = col+j
            if m<0 or m>numrows-1 or n<0 or n>numcols-1:
                continue
                
            while seats[m][n] == '.':
                m+=i
                n+=j
                if m<0 or m>numrows-1 or n<0 or n>numcols-1:
                    m-=i
                    n-=j
                    break
            
            if seats[m][n] == '#':
                adj += 1
    return adj

def get_num_adjacent_occ_seats(row,col):
    adj = 0
    for i in range(row-1,row+2):        
        for j in range(col-1,col+2):
            if i == row and j==col:
                continue
            elif i == -1 or i==numrows: # Top or bottom row
                if j==-1:
                    continue
                elif j == numcols: # Top right or bottom corner
                    continue
                else:
                    continue
            elif j==-1 or j==numcols:
                # left or right columns, but not a corner
                continue
            elif seats[i][j] == '#':
                adj += 1
    return adj

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 11")
    with open(inputfile, 'r') as f:
        seats = [list(line.strip()) for line in f.readlines()]

    done = 0
    new_seats = copy.deepcopy(seats)
    numrows = len(new_seats)
    numcols = len(new_seats[0])

    do_part1 = 0
    if do_part1:
        while (not done):
            done = 1
            seats = copy.deepcopy(new_seats)
            for row in range(0,len(seats)):
                for col in range(0,numcols):
                    if seats[row][col] == 'L':
                        # Seat is empty - check the adjacent seats
                        if get_num_adjacent_occ_seats(row,col) == 0:
                            new_seats[row][col] = '#'
                            done = 0
                    elif seats[row][col] == '#':
                        # Seat is occupied - check for 4 or more adjacent seats
                        if get_num_adjacent_occ_seats(row,col) >= 4:
                            new_seats[row][col] = 'L'
                            done = 0
        part1 = 0
        for row in seats:
            part1 += row.count("#")
        print("Part 1:", part1)
        
    
    while (not done):
        done = 1
        seats = copy.deepcopy(new_seats)
        for row in range(0,len(seats)):
            for col in range(0,numcols):
                #print(row,col)
                if seats[row][col] == 'L':
                    # Seat is empty - check the adjacent seats
                    if getpart2(row,col) == 0:
                        new_seats[row][col] = '#'
                        done = 0
                elif seats[row][col] == '#':
                    # Seat is occupied - check for 4 or more adjacent seats
                    if getpart2(row,col) >= 5:
                        new_seats[row][col] = 'L'
                        done = 0       
    part2 = 0
    for row in seats:
        part2 += row.count("#")
    print("Part 2:", part2)