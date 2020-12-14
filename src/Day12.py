#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
inputfile = "input/Day12Input.txt"
waypoint_loc = []

def rotate_waypoint(direction,dist):
    if dist==90 and direction=='R' or dist==270 and direction=='L':
        tmp = waypoint_loc[0]
        waypoint_loc[0]=-1*waypoint_loc[1]
        waypoint_loc[1]=tmp    
    elif dist == 180:
        waypoint_loc[0] *= -1
        waypoint_loc[1] *= -1        
    else:
        tmp = waypoint_loc[0]
        waypoint_loc[0]=waypoint_loc[1]
        waypoint_loc[1]=-1*tmp
        

if __name__ == "__main__":
    print("Advent of Code 2020 - Day 12")
    with open(inputfile, 'r') as f:
        data = [[line.strip()[0], int(line.strip()[1:])] for line in f.readlines()]

    cur_dir = 90 # 0 == north, 90 == east, 180 == south, 270 == west
    cur_loc = [0,0] # north, east
    for action, dist in data:
        if action == 'N':
            cur_loc[0] += dist            
        elif action == 'S':
            cur_loc[0] -= dist
        elif action == 'E':
            cur_loc[1] += dist
        elif action == 'W':
            cur_loc[1] -= dist
        elif action == 'L':
            cur_dir -= dist
        elif action == 'R':
            cur_dir += dist
        else:
            if cur_dir == 0:
                cur_loc[0] += dist
            elif cur_dir == 90:
                cur_loc[1] += dist
            elif cur_dir == 180:
                cur_loc[0] -= dist
            else:
                cur_loc[1] -= dist
                
        if cur_dir >= 360:
            cur_dir -= 360
        elif cur_dir < 0:
            cur_dir += 360        
    print("Part 1:", abs(cur_loc[0]) + abs(cur_loc[1]))
    
    ship_loc = [0,0] #north, east
    waypoint_loc = [1,10]
    waypoint_dir = 0

    for action, dist in data:
        if action == 'N':
            waypoint_loc[0] += dist            
        elif action == 'S':
            waypoint_loc[0] -= dist
        elif action == 'E':
            waypoint_loc[1] += dist
        elif action == 'W':
            waypoint_loc[1] -= dist
        elif action in ['L', 'R']:
            rotate_waypoint(action, dist)
        elif action == 'F':
            ship_loc[0] += dist*waypoint_loc[0]
            ship_loc[1] += dist*waypoint_loc[1]
                
    print("Part 2:", abs(ship_loc[0]) + abs(ship_loc[1]))
    