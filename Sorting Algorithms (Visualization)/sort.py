from functions import get_random_number_list
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, heap_sort, merge_sort, radix_sort, quick_sort

if __name__ == "__main__":
    list_size = 100
    randomized_list = get_random_number_list(size=list_size)
    bubble_sort(randomized_list=randomized_list.copy())
    selection_sort(randomized_list=randomized_list.copy())
    insertion_sort(randomized_list=randomized_list.copy())
    heap_sort(randomized_list=randomized_list.copy())
    merge_sort(randomized_list=randomized_list.copy())
    radix_sort(randomized_list=randomized_list.copy())
    quick_sort(randomized_list=randomized_list.copy())