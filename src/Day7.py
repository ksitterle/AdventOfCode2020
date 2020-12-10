
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

inputfile = "input/Day7Input.txt"
gold_bag_containers = ["shiny gold bag"]
updates = 1
bag_dict = {}

# returns the total count of bags inside this bag including this bag
# this_bag is a string name of the bag
def count_bag_totals(this_bag):
    ret = 0
    for internal_bag_k, internal_bag_v in bag_dict[this_bag].items():
        ret += int(internal_bag_v) * count_bag_totals(internal_bag_k)
    
    print(this_bag, "has", ret)
    return (ret + 1) # Add one to include THIS bag

# Returns true if a gold bag or gold bag container was found
# this_bag is a dictionary of the bag's contents
def find_gold_bags(this_bag):
    for bag_type in gold_bag_containers:
        if bag_type in this_bag.keys():
            #print("found a match", bag_type)
            return 1
    return 0

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 7")
    with open(inputfile, 'r') as f:
        rules = f.readlines()

    # Build dictionary of rules
    for line in rules:
        # Example: line = muted white bags contain 3 muted tomato bags, 5 light black bags, 4 pale black bags, 5 shiny gold bags.
        bag_name = line.split("contain")[0].rstrip().replace("bags", "bag")
        contents = line.split("contain")[1].split(",")
        # Example: contents = [3 muted tomato bags, 5 light black bags, 4 pale black bags, 5 shiny gold bags.]     
        contents_dict = {}
        for contents_bag in contents:
            # Example: contents_bag = 5 shiny gold bags.
            contents_bag = contents_bag.lstrip().rstrip()
            if contents_bag == "no other bags.": break
            internal_bag_name = contents_bag[2:].replace(".","").replace("bags", "bag")
            contents_dict[internal_bag_name] = contents_bag[0]
            
        bag_dict[bag_name] = contents_dict
                           
    # Find the gold bags within gold bags
    while(updates):
        updates = 0
        for k, v in bag_dict.items():
            if find_gold_bags(v):
                #print("found a match for", k)
                if k not in gold_bag_containers:
                    gold_bag_containers.append(k)
                    #print("new list:", gold_bag_containers)
                    updates = 1
    
    print("Part 1: Number possible bag colors is", len(gold_bag_containers)-1) # -1 to remove "Shiny gold bag"    
    print("Part 2: Total num bags required is", count_bag_totals("shiny gold bag")-1) # -1 to remove gold bag from the final count
    