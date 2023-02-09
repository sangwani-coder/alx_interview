#!/bin/env python3

"""
    Finds the number of teaspoons that makes a cake too sweet.

    n - the number of teaspoons of sugar that the recipe states is
        required to make the cake

    isTooSweet(i): returns true if i teaspoons of sugar makes the cake
        too sweet.
    x - the first number of teaspoons of sugar that make 
        the cake too sweet.
"""

def isTooSweet(i):
    """
        finds x, the first number of teaspoons that make
        the cake too sweet.
    """
    # After x the cake is too swweet
    # n is superior or equal to 1
    # for any value of n, your cake will always be 
    # too sweet( x always exists)

    n = int(input())
    if n >= 1:
        if i == n:
            x = i
            return True
        if i > n:
            for j in range(i):
                if j == n:
                    x = j
            return True
        if i < n:
            x = n
