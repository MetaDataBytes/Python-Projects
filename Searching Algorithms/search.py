from functions import get_number_list, quick_sort
from searching_algorithms import linear_search, jump_search, binary_search, ternary_search, interpolation_search, exponential_search
import random

if __name__ == "__main__": 
    # CREATE LIST TO SEARCH THROUGH AND CHOICE SEARCH VALUE
    size = 10_000
    sorted_list = quick_sort(randomized_list=get_number_list(size=size))
    search_value = random.choice(sorted_list)

    # SEARCH
    linear_search_index = linear_search(search_list=sorted_list, search_value=search_value)
    jump_search_index = jump_search(search_list=sorted_list, search_value=search_value)
    binary_search_index = binary_search(search_list=sorted_list, search_value=search_value)
    ternary_search_index = ternary_search(search_list=sorted_list, search_value=search_value)
    interpolation_search_index = interpolation_search(search_list=sorted_list, search_value=search_value)
    exponential_search_index = exponential_search(search_list=sorted_list, search_value=search_value)

    # RESULTS
    print(f"Searched for: {search_value:,}")
    print(f"Linear Search Results: {f"{sorted_list[linear_search_index]:,}" if linear_search_index > -1 else f"{search_value:,} not found!"}")
    print(f"Jump Search Results: {f"{sorted_list[jump_search_index]:,}" if jump_search_index > -1 else f"{search_value:,} not found!"}")
    print(f"Binary Search Results: {f"{sorted_list[binary_search_index]:,}" if binary_search_index > -1 else f"{search_value:,} not found!"}")
    print(f"Ternary Search Results: {f"{sorted_list[ternary_search_index]:,}" if ternary_search_index > -1 else f"{search_value:,} not found!"}")
    print(f"Interpolation Search Results: {f"{sorted_list[interpolation_search_index]:,}" if interpolation_search_index > -1 else f"{search_value:,} not found!"}")
    print(f"Exponential Search Results: {f"{sorted_list[exponential_search_index]:,}" if exponential_search_index > -1 else f"{search_value:,} not found!"}")