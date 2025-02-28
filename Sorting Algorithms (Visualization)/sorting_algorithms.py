from functions import show_sorting, validate_sorting
from typing import Union

def bubble_sort(randomized_list: list[any]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the bubble sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """
    list_size = len(randomized_list)
    for a_idx in range(list_size):
        for b_idx in range(0, list_size - a_idx - 1):
            if randomized_list[b_idx] > randomized_list[b_idx + 1]: 
                randomized_list[b_idx], randomized_list[b_idx + 1] = randomized_list[b_idx + 1], randomized_list[b_idx]
                show_sorting(idx=[b_idx, b_idx + 1], algorithm="Bubble Sort O(n^2): ", list_of_numbers=randomized_list)
    validate_sorting(algorithm="Bubble Sort O(n^2): ", list_of_numbers=randomized_list)
    return randomized_list

def selection_sort(randomized_list: list[any]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the selection sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """
    list_size = len(randomized_list)
    for a_idx in range(list_size - 1):
        min_idx = a_idx
        for b_idx in range(a_idx + 1, list_size): 
            if randomized_list[b_idx] < randomized_list[min_idx]: min_idx = b_idx
        randomized_list[a_idx], randomized_list[min_idx] = randomized_list[min_idx], randomized_list[a_idx]
        show_sorting(idx=[a_idx, min_idx], algorithm="Selection Sort O(n^2): ", list_of_numbers=randomized_list)
    validate_sorting(algorithm="Selection Sort O(n^2): ", list_of_numbers=randomized_list)
    return randomized_list

def insertion_sort(randomized_list: list[any]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the insertion sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """
    for a_idx in range(1, len(randomized_list)):
        key = randomized_list[a_idx]
        b_idx = a_idx - 1
        while b_idx >= 0 and key < randomized_list[b_idx]:
            randomized_list[b_idx + 1] = randomized_list[b_idx]
            b_idx -= 1
        randomized_list[b_idx + 1] = key
        show_sorting(idx=[a_idx, b_idx + 1], algorithm="Insertion Sort O(n^2): ", list_of_numbers=randomized_list)
    validate_sorting(algorithm="Insertion Sort O(n^2): ", list_of_numbers=randomized_list)
    return randomized_list

def heap_sort(randomized_list: list[any]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the heap sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """
    list_size = len(randomized_list)
    for a_idx in range(list_size // 2 - 1, -1, -1): heap_sort_heapify(randomized_list, list_size, a_idx)
    for b_idx in range(list_size - 1, 0, -1):
        randomized_list[b_idx], randomized_list[0] = randomized_list[0], randomized_list[b_idx]
        heap_sort_heapify(randomized_list, b_idx, 0)
        show_sorting(idx=[a_idx, 0], algorithm="Heap Sort O(n log(n)): ", list_of_numbers=randomized_list)
    validate_sorting(algorithm="Heap Sort O(n log(n)): ", list_of_numbers=randomized_list)
    return randomized_list
        
def heap_sort_heapify(randomized_list: list[any], list_size: int, a_idx: int) -> list[any]:
    """
    PURPOSE: Split the list in left and right and place in order\n
    ARGUMENT: random_number_list (list): list to be sorted, list_size (int): size of list, a_idx (int): index for finding largest element in list\n
    RETURN: random_number_list (list): list being sorted\n
    """
    largest = a_idx
    left = 2 * a_idx + 1
    right = 2 * a_idx + 2

    if left < list_size and randomized_list[largest] < randomized_list[left]: largest = left
    if right < list_size and randomized_list[largest] < randomized_list[right]: largest = right
    if largest != a_idx:
        randomized_list[a_idx], randomized_list[largest] = randomized_list[largest], randomized_list[a_idx]
        heap_sort_heapify(randomized_list, list_size, largest)
        show_sorting(idx=[a_idx, largest], algorithm="Heap Sort O(n log(n)): ", list_of_numbers=randomized_list)
    return randomized_list

def merge_sort(randomized_list: list[any]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the merge sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """

    randomized_list = merge_sort_sort(randomized_list=randomized_list, left=0, right=len(randomized_list) - 1)
    validate_sorting(algorithm="Merge Sort O(n logn): ", list_of_numbers=randomized_list)
    return randomized_list

def merge_sort_sort(randomized_list: list[any], left: int, right: int) -> list[any]:
    """
    PURPOSE: Sort the provided list by breaking the list into left and right\n
    ARGUMENT: random_number_list (list): the list to be sorted, left (int): the low end of the list, right (int): the high end of the list\n
    RETURN: (list): the sorted list\n
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort_sort(randomized_list, left, mid)
        show_sorting(idx=[left, mid], algorithm="Merge Sort O(n logn): ", list_of_numbers=randomized_list)
        merge_sort_sort(randomized_list, mid + 1, right)
        show_sorting(idx=[mid + 1, right], algorithm="Merge Sort O(n logn): ", list_of_numbers=randomized_list)
        merge_sort_merge(randomized_list, left, mid, right)
        show_sorting(idx=[left, mid, right], algorithm="Merge Sort O(n logn): ", list_of_numbers=randomized_list)
    return randomized_list

def merge_sort_merge(randomized_list: list[any], left: int, mid: int, right: int) -> list[any]:
    """
    PURPOSE: Merge the left and right sides of the random list by order\n
    ARGUMENT: random_number_list (list): list being sorted, left (int): index of left side, mid (int): index of mid-point, right (int): index of right side\n
    RETURN: random_number_list (list): list being sorted\n
    """
    left_idx = mid - left + 1
    right_idx = right - mid

    L = [randomized_list[left + i] for i in range(left_idx)]
    R = [randomized_list[mid + 1 + j] for j in range(right_idx)]

    a_idx, b_idx, c_idx = 0, 0, left

    while a_idx < left_idx and b_idx < right_idx:
        if L[a_idx] <= R[b_idx]:
            randomized_list[c_idx] = L[a_idx]
            a_idx += 1
        else:
            randomized_list[c_idx] = R[b_idx]
            b_idx += 1
        c_idx += 1

    while a_idx < left_idx:
        randomized_list[c_idx] = L[a_idx]
        a_idx += 1
        c_idx += 1

    while b_idx < right_idx:
        randomized_list[c_idx] = R[b_idx]
        b_idx += 1
        c_idx += 1
    return randomized_list

def radix_sort(randomized_list: list[Union[int, float]]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the radix sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """
    largest = max(randomized_list)
    exponent = 1
    while largest / exponent >= 1:
        list_size = len(randomized_list)
        output = [0] * list_size
        count_array = [0] * 10

        for a_idx in range(list_size):
            index = randomized_list[a_idx] // exponent
            count_array[index % 10] += 1

        for b_idx in range(1,10): count_array[b_idx] += count_array[b_idx - 1]
        
        max_idx = list_size - 1
        while max_idx >= 0:
            index = randomized_list[max_idx] // exponent
            output[count_array[index % 10] - 1] = randomized_list[max_idx]
            count_array[index % 10] -= 1
            max_idx -= 1
        
        for c_idx in range(0, len(randomized_list)): 
            randomized_list[c_idx] = output[c_idx]
            show_sorting(idx=[c_idx], algorithm="Radix Sort O(d*(n+b)): ", list_of_numbers=randomized_list)
        exponent *=10
    validate_sorting(algorithm="Radix Sort O(d*(n+b)): ", list_of_numbers=randomized_list)
    return randomized_list

def quick_sort(randomized_list: list[any]) -> list[any]:
    """
    PURPOSE: Sort the provided list using the quick sort algorithm\n
    ARGUMENT: random_number_list (list): the list to be sorted\n
    RETURN: (list): the sorted list\n
    """
    stack = [(0, len(randomized_list) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = quick_sort_partition(randomized_list, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    validate_sorting(algorithm="Quick Sort O(n log(n)): ", list_of_numbers=randomized_list)
    return randomized_list

def quick_sort_partition(randomized_list: list[any], low: int, high: int) -> int:
    """
    PURPOSE: Sort the randomized_list around it's pivot\n
    ARGUMENT: randomized_list (list): list being sorted, low (int): lowest element in list, high (int): highest element in list\n
    RETURN: (int) the index of the pivot + 1\n
    """
    pivot = randomized_list[high]
    i = low - 1
    for j in range(low, high):
        if randomized_list[j] <= pivot:
            i += 1
            randomized_list[i], randomized_list[j] = randomized_list[j], randomized_list[i]
            show_sorting(idx=[i, j], algorithm="Quick Sort O(n log(n)): ", list_of_numbers=randomized_list)
    randomized_list[i + 1], randomized_list[high] = randomized_list[high], randomized_list[i + 1]
    show_sorting(idx=[i + 1, high], algorithm="Quick Sort O(n log(n)): ", list_of_numbers=randomized_list)
    return i + 1