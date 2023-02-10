#!/bin/env python3

""" Problem #2"""


def max_distance():
    fields = [1,2,3,4]
    towers = [1,4]
    max_dist = towers[0] - fields[0]
    
    for i in range(len(towers)):
        for j in range(len(fields)):
            temp = towers[i] - fields[j]
            if temp >= max_dist:
                max_dist = temp
    return max_dist
print(max_distance())
