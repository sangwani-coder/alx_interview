#!/bin/env python3

"""
    Problem #1
"""
N = int(input())

single_key_press_3 = 3
single_key_press_4 = 4
single_key_press_5 = 5

non_print_presses = 2

def problem_1():
    if N < 7:
        return N
    printing_presses = N - non_print_presses

    c_v_combin = printing_presses - single_key_press_3

    total_c_v_output = c_v_combin * single_key_press_3

    output =  total_c_v_output + single_key_press_3

    return output

print(problem_1())
