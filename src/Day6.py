
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day6Input.txt"


if __name__ == "__main__":
    print("Advent of Code 2020 - Day 6")
    with open(inputfile, 'r') as f:
        data = f.readlines()
        
    totals_pt1, totals_pt2 = [], []
    group_ans = ""
    group_sum_pt1, group_sum_pt2,  num_group_members = 0, 0, 0
        
    for line in data:
        if line.strip():
            group_ans += line.strip()
            num_group_members += 1
        else:
            for i in range(ord('a'), ord('z')+1):
            # Part 1
                group_sum_pt1 += 1 if chr(i) in group_ans else 0
            # Part 2
                group_sum_pt2 += 1 if group_ans.count(chr(i)) == num_group_members else 0
            
            totals_pt1.append(group_sum_pt1)
            totals_pt2.append(group_sum_pt2)
            group_ans = ""
            group_sum_pt1, group_sum_pt2,  num_group_members = 0, 0, 0
        
    print("Part 1:", sum(totals_pt1))
    print("Part 2:", sum(totals_pt2))