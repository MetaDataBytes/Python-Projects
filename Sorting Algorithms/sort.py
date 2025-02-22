from functions import get_random_number_list, get_random_string_list, test_sorted_order
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, heap_sort, merge_sort, radix_sort, quick_sort


# CREATE RANDOM LIST
list_size = 10_000
random_number_list = get_random_number_list(size=list_size)
#random_string_list = get_random_string_list(size=list_size)

# SORT RANDOM LIST
bubble_sort_list = bubble_sort(random_number_list=random_number_list.copy())
selection_sort_list = selection_sort(random_number_list=random_number_list.copy())
insertion_sort_list = insertion_sort(random_number_list=random_number_list.copy())
heap_sort_list = heap_sort(random_number_list=random_number_list.copy())
merge_sort_list = merge_sort(random_number_list=random_number_list.copy())
radix_sort_list = radix_sort(random_number_list=random_number_list.copy())
quick_sort_list = quick_sort(random_number_list=random_number_list.copy())

# CHECK IF LIST ARE SORTED
print(f"Buble Sort List sorted: {test_sorted_order(list=bubble_sort_list)}")
print(f"Selection Sort List sorted: {test_sorted_order(list=selection_sort_list)}")
print(f"Insertion Sort List sorted: {test_sorted_order(list=insertion_sort_list)}")
print(f"Heap Sort List sorted: {test_sorted_order(list=heap_sort_list)}")
print(f"Merge Sort List sorted: {test_sorted_order(list=merge_sort_list)}")
print(f"Radix Sort List sorted: {test_sorted_order(list=radix_sort_list)}")
print(f"Quick Sort List sorted: {test_sorted_order(list=quick_sort_list)}")