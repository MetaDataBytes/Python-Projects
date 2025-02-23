from typing import Union
from math import sqrt

def linear_search(search_list: list[any], search_value: any) -> int:
    """
    PURPOSE: Perform a linear search to find the search value in the search list\n
    ARGUMENT: search_list (list): A list to search through, search_value (any): the value to search for\n
    RETURN: (int): The index location of the search value. -1 indicates value is not found\n
    """
    for idx, element in enumerate(search_list):
        if element == search_value: return idx
    return -1

def jump_search(search_list: list[any], search_value: any) -> int:
    """
    PURPOSE: Perform a jump search to find the search value in the search list\n
    ARGUMENT: search_list (list): A list to search through, search_value (any): the value to search for\n
    RETURN: (int): The index location of the search value. -1 indicates value is not found\n
    """
    search_list_length = len(search_list)
    jump = int(sqrt(search_list_length))
    previous = 0

    while search_list[int(min(jump, search_list_length) - 1)] < search_value:
        if previous > search_list_length - 1: return -1
        else: 
            previous = jump
            jump += int(sqrt(search_list_length))

    while search_list[int(previous)] < search_value: previous += 1
    if search_list[int(previous)] == search_value: return int(previous)
    else: return -1

def binary_search(search_list: list[any], search_value: any) -> int:
    """
    PURPOSE: Perform a binary search to find the search value in the search list\n
    ARGUMENT: search_list (list): A list to search through, search_value (any): the value to search for\n
    RETURN: (int): The index location of the search value. -1 indicates value is not found\n
    """
    left = 0
    right = len(search_list)

    while left < right:
        middle = (left + right) // 2
        if search_list[middle] == search_value: return middle
        elif search_list[middle] < search_value: left = middle + 1
        else: right = middle - 1
    return -1

def ternary_search(search_list: list[any], search_value: any) -> int:
    """
    PURPOSE: Perform a ternary search to find the search value in the search list\n
    ARGUMENT: search_list (list): A list to search through, search_value (any): the value to search for\n
    RETURN: (int): The index location of the search value. -1 indicates value is not found\n
    """
    left = 0
    right = len(search_list) - 1
    
    while (right >= left):
        middle_0 = left + (right - left) // 3
        middle_1 = right - (right - left) // 3

        if (search_list[middle_0] == search_value): return middle_0
        elif (search_list[middle_1] == search_value): return  middle_1
        elif (search_value < search_list[middle_0]): right = middle_0 - 1
        elif (search_value > search_list[middle_1]): left = middle_1 + 1
        else: left, right = middle_0 + 1, middle_1 - 1
    return -1

def interpolation_search(search_list: list[Union[float, int]], search_value: any) -> int:
    """
    PURPOSE: Perform a interpolation search to find the search value in the search list\n
    ARGUMENT: search_list (list): A list to search through, search_value (any): the value to search for\n
    RETURN: (int): The index location of the search value. -1 indicates value is not found\n
    """
    low = 0
    high = len(search_list) - 1
    
    while low <= high and search_value >= search_list[low] and search_value <= search_list[high]:
        if low == high:
            if search_list[low] == search_value: return low
            else: return -1
            
        middle = low + ((high - low) // (search_list[high] - search_list[low]) * (search_value - search_list[low]))
        if search_list[middle] == search_value: return middle
        elif search_list[middle] < search_value: low = middle + 1
        elif search_list[middle] > search_value: high = middle - 1
    return -1

def exponential_search(search_list: list[any], search_value: any) -> int:
    """
    PURPOSE: Perform a exponential search to find the search value in the search list\n
    ARGUMENT: search_list (list): A list to search through, search_value (any): the value to search for\n
    RETURN: (int): The index location of the search value. -1 indicates value is not found\n
    """
    length = len(search_list)
    if search_list[0] == search_value: return 0
    else: index = 1
    while index < length and search_list[index] <= search_value: index *= 2
    
    left = index // 2
    right = min(index, length - 1)

    while left <= right:
        middle = (left + right) // 2
        if search_list[middle] == search_value: return middle
        elif search_list[middle] < search_value: left = middle + 1
        else: right = middle - 1
    return -1