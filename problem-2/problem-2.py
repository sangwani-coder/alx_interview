#!/bin/env python3

""" 
    Problem #2

"""

def max_distance(fields=[], towers=[]):
    """
        function that returns max power needed for
        the list of fields and water towers.
    """

    max_dist = towers[0] - fields[0]
    
    for i in range(len(towers)):
        for j in range(len(fields)):
            temp = towers[i] - fields[j]
            if temp >= max_dist:
                max_dist = temp
    return max_dist

#test
#print(max_distance([1,2,3],[2]))=> 1
#print(max_distance([1,2,3,4],[1,4]))=> 3
#print(max_distance([1,5],[10]))=> 9
