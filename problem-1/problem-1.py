#!/bin/env python3

"""
    Problem #1
    find out the maximun numbers of 'A' you
    can print on screen.
"""
# Input N = 2
    # output = 2 -> for: A, A

# Input: N = 12
# Output: 30 -> for the sequence
    # A, A, A, A, A Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V, Ctrl-V, Ctrl-V, Ctrl-V

N = int(input())

# number of keys not printing
key2_key3_presses = 2


def check_max():
    """
        finds the maximum number of 'A' you can print on screen.
    """
    largest = check_key_combination(3)

    for i in range(4, N + 1):
        temp = check_key_combination(i)

        if largest < temp:
            largest = temp
    return largest


def check_key_combination(key1_A):
    """
        function to calculate key combinations to
        print max number of A's on screen.
    """

    if N < 7:
        return N
    printing_presses = N - key2_key3_presses

    key4_c_v = printing_presses - key1_A

    total_c_v_output = key4_c_v * key1_A

    output = total_c_v_output + key1_A

    return output
 
#print(check_max())
