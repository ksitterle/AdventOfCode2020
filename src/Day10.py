#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputfile = "input/Day10Input.txt"

# Dictionary mapping goal joltages to potential adapters
jolt_dict = {}

# Ending voltage we're searching for
goal_jolt = 0 

# Dictionary keeping track of previously calculated adapter paths
# [adapter] = [num_good_endings, done boolean]
known_good_endings = {}

# Returns the number of combinations that work from this joltage
# This is not efficient, but it works!  
def brute_force_part2(joltage):    
    if joltage == goal_jolt:
        return 1
    elif joltage > goal_jolt:
        return 0
    ans = 0
    for adapter in jolt_dict[joltage]:
        ans += brute_force_part2(adapter)        
    return ans

# More efficient - don't recalculate any endings that were already counted
def part2(joltage):
    # If this one is already done, return the number of good endings from here
    # [num good endings, done]
    if joltage in known_good_endings:
        if known_good_endings[joltage][1]:
            return known_good_endings[joltage][0]
    
    ans = 0
    for adapter in jolt_dict[joltage]:
        ans += part2(adapter)
        
    # This ending is done!
    if joltage in known_good_endings:
        known_good_endings[joltage][1] = 1
        known_good_endings[joltage][0] = ans
    return ans


if __name__ == "__main__":
    print("Advent of Code 2020 - Day 10")
    with open(inputfile, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]

    data.sort()
    goal_jolt = max(data)+3
    data.append(goal_jolt)
    
       
    # Part 1
    current_jolt = 0
    joltdiff1 = 0
    joltdiff3 = 0
    for adapter in data:
        if adapter-1 == current_jolt:
            current_jolt += 1
            joltdiff1 += 1
        elif adapter - 2 == current_jolt:
            current_jolt += 2
        elif adapter-3 == current_jolt:
            current_jolt += 3
            joltdiff3 += 1
                
    print("Part 1:", joltdiff1*joltdiff3)
    
    # Part 2
    # Create the goal_joltage to adaptors dictionary
    for adapter in data:
        for i in range(adapter-3, adapter):
            if i in jolt_dict:
                jolt_dict[i].append(adapter)
            else:
                jolt_dict[i]=[adapter]            
        known_good_endings[adapter] = [0,0]
        
    # Set goal voltage to done with 1 potential path to success
    known_good_endings[goal_jolt] = [1,1]
    
    print("Part 2:", part2(0))
    