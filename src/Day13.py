#!/usr/bin/env python
# -*- coding: utf-8 -*-
inputfile = "input/Day13Input.txt"
import numpy as np
          
if __name__ == "__main__":
    print("Advent of Code 2020 - Day 13")
    with open(inputfile, 'r') as f:
        data = f.readlines()
          
    earliest = float(data[0].strip())
    busIDs = data[1].strip().split(",")
          
    timestamp = earliest
    done = 0
    while not done:
        for bus in busIDs:
            if bus == 'x':
                continue
            if timestamp % int(bus) == 0:
                print("Part 1:", (timestamp - earliest)*float(bus))
                done = 1
        timestamp += 1
          
    busIDfloats = [float(i) for i in busIDs if i != 'x']
    schedules = []
    for bus in busIDfloats:
        schedules.append(busIDs.index(str(int(bus))))
    
    t = busIDfloats[0]
    for i in range(1, len(schedules)):
        while (t + schedules[i]) % busIDfloats[i]:
            t += np.prod(busIDfloats[:i])
    print("Part 2", t)
    