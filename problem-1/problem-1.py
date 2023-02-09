#!/bin/env python3

"""
    Problem #1
"""

N = int(input())
non_print_presses = 2


def check_max():
    """
        finds the maximum number of 'A' you can print on screen.
    """
    output1 = check_key_combination(3)
    output2 = check_key_combination(4)
    output3 = check_key_combination(5)

    if output1 >= output2 and output1 >= output3:
        largest = output1
    elif output2 >= output1 and output2 >= output3:
        largest = output2
    else:
        largest = output3

    return largest


def check_key_combination(single_key_press):
    """
        function to calculate key combinations to
        print max number of A's on screen.
    """

    if N < 7:
        return N
    printing_presses = N - non_print_presses

    c_v_combin = printing_presses - single_key_press

    total_c_v_output = c_v_combin * single_key_press

    output = total_c_v_output + single_key_press

    return output
 
print(check_max())
