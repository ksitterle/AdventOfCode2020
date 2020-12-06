
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re

inputfile = "input/Day4Input.txt"
passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

# ret 1 if valid, 0 if invalid
def validate_entry(entry):
    for key, value in entry.items():
        if key == "byr" and not (1920 <= int(value) <= 2002):
            return 0
        if key == "iyr" and not (2010 <= int(value) <= 2020):
            return 0
        if key == "eyr" and not (2020 <= int(value) <= 2030):
            return 0
        if key == "hgt":
            if "cm" in value and not (150 <= int(value.replace("cm", "")) <= 193):
                return 0
            if "in" in value and not (59 <= int(value.replace("in", "")) <= 76):
                return 0
            elif "in" not in value and "cm" not in value:
                print(key,value)
                return 0
        if key == "hcl":
            if value[0] != "#":  
                return 0
            if len(value[1:]) != 6:
                return 0
            hairlist = re.findall("[^0-9a-f]", value[1:])
            if len(hairlist) != 0:
                return 0
        if key == "ecl" and value not in eyecolors:
            return 0
        if key == "pid" and not len(value) == 9:
            return 0
                
        
    return 1


if __name__ == "__main__":
    print("Advent of Code 2020 - Day 4")
    valid_passport_count = 0
    with open(inputfile) as f:
        data = f.readlines()
                
    passport_entry = "" 
    entries = []
    dict = {}
    for i in range(0, len(data)):
        if data[i] != "\n": 
            passport_entry += " " + (data[i].strip())
        else:      
            for entry in passport_entry.split():
                key = entry[0:entry.find(":")]
                dict[key] = entry[entry.find(":")+1:]
                
            entries.append(dict)
            passport_entry = ""
            dict = {}
            

    for entry in entries:
        valid_field_count = 0
        if len(entry) == 8 or len(entry) == 7:
            for field in passport_fields:
                if field in entry:
                    valid_field_count += 1
                    
            if valid_field_count == 8:
                if validate_entry(entry) == 0:
                    print("Invalid!\n", entry)
                else:
                    valid_passport_count += 1
            elif valid_field_count == 7:
                if "cid" not in entry:
                    if validate_entry(entry) == 0:
                        print("Invalid!\n", entry)
                    else:
                        valid_passport_count += 1
        
    print(valid_passport_count)
        

