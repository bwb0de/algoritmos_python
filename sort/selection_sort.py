#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# license: AGPL-3.0 
#

def find_minimum(input_list, initial_index=0, return_element=False):
    
    current_minimal_element_index = initial_index
    
    for element_index in range(initial_index, len(input_list)):
        if input_list[element_index] < input_list[current_minimal_element_index]:
            current_minimal_element_index = element_index
    
    if return_element:
        return input_list[current_minimal_element_index]
    return current_minimal_element_index


def selection_sort(input_list):
    
    for element_index in range(len(input_list)):
        minimum_index = find_minimum(input_list, initial_index=element_index)
        input_list[element_index], input_list[minimum_index] = input_list[minimum_index], input_list[element_index]

    return input_list


