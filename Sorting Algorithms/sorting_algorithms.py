def bubble_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the bubble sort algorithm
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    list_size = len(random_number_list)
    for a_idx in range(list_size):
        for b_idx in range(0, list_size - a_idx - 1):
            if random_number_list[b_idx] > random_number_list[b_idx + 1]: random_number_list[b_idx], random_number_list[b_idx + 1] = random_number_list[b_idx + 1], random_number_list[b_idx]
    return random_number_list

def selection_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the selection sort algorithm
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    list_size = len(random_number_list)
    for a_idx in range(list_size - 1):
        min_idx = a_idx
        for b_idx in range(a_idx + 1, list_size): 
            if random_number_list[b_idx] < random_number_list[min_idx]: min_idx = b_idx
        random_number_list[a_idx], random_number_list[min_idx] = random_number_list[min_idx], random_number_list[a_idx]
    return random_number_list

def insertion_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the insertion sort algorithm
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    for a_idx in range(1, len(random_number_list)):
        key = random_number_list[a_idx]
        b_idx = a_idx - 1
        while b_idx >= 0 and key < random_number_list[b_idx]:
            random_number_list[b_idx + 1] = random_number_list[b_idx]
            b_idx -= 1
        random_number_list[b_idx + 1] = key
    return random_number_list

def heap_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the heap sort algorithm
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    list_size = len(random_number_list)
    for a_idx in range(list_size // 2 - 1, -1, -1): heap_sort_heapify(random_number_list, list_size, a_idx)
    for b_idx in range(list_size - 1, 0, -1):
        random_number_list[b_idx], random_number_list[0] = random_number_list[0], random_number_list[b_idx]
        heap_sort_heapify(random_number_list, b_idx, 0)
    return random_number_list
        
def heap_sort_heapify(random_number_list: list, list_size: int, a_idx: int) -> list:
    """
    PURPOSE: Split the list in left and right and place in order
    ARGUMENT: random_number_list (list): list to be sorted, list_size (int): size of list, a_idx (int): index for finding largest element in list
    RETURN: random_number_list (list): list being sorted
    """
    largest = a_idx
    left = 2 * a_idx + 1
    right = 2 * a_idx + 2

    if left < list_size and random_number_list[largest] < random_number_list[left]: largest = left
    if right < list_size and random_number_list[largest] < random_number_list[right]: largest = right
    if largest != a_idx:
        random_number_list[a_idx], random_number_list[largest] = random_number_list[largest], random_number_list[a_idx]
        heap_sort_heapify(random_number_list, list_size, largest)
    return random_number_list

def merge_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the merge sort algorithm
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    return merge_sort_sort(random_number_list=random_number_list, left=0, right=len(random_number_list) - 1)

def merge_sort_sort(random_number_list: list, left: int, right: int) -> list:
    """
    PURPOSE: Sort the provided list by breaking the list into left and right
    ARGUMENT: random_number_list (list): the list to be sorted, left (int): the low end of the list, right (int): the high end of the list
    RETURN: (list): the sorted list
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort_sort(random_number_list, left, mid)
        merge_sort_sort(random_number_list, mid + 1, right)
        merge_sort_merge(random_number_list, left, mid, right)
    return random_number_list

def merge_sort_merge(random_number_list: list, left: int, mid: int, right: int) -> list:
    """
    PURPOSE: Merge the left and right sides of the random list by order
    ARGUMENT: random_number_list (list): list being sorted, left (int): index of left side, mid (int): index of mid-point, right (int): index of right side
    RETURN: random_number_list (list): list being sorted
    """
    left_idx = mid - left + 1
    right_idx = right - mid

    L = [random_number_list[left + i] for i in range(left_idx)]
    R = [random_number_list[mid + 1 + j] for j in range(right_idx)]

    a_idx, b_idx, c_idx = 0, 0, left

    while a_idx < left_idx and b_idx < right_idx:
        if L[a_idx] <= R[b_idx]:
            random_number_list[c_idx] = L[a_idx]
            a_idx += 1
        else:
            random_number_list[c_idx] = R[b_idx]
            b_idx += 1
        c_idx += 1

    while a_idx < left_idx:
        random_number_list[c_idx] = L[a_idx]
        a_idx += 1
        c_idx += 1

    while b_idx < right_idx:
        random_number_list[c_idx] = R[b_idx]
        b_idx += 1
        c_idx += 1
    return random_number_list

def radix_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the radix sort algorithm. CAN ONLY SORT NUMBERS
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    largest = max(random_number_list)
    exponent = 1
    
    while largest / exponent >= 1:
        list_size = len(random_number_list)
        output = [0] * list_size
        count_array = [0] * 10

        for a_idx in range(list_size):
            index = random_number_list[a_idx] // exponent
            count_array[index % 10] += 1

        for b_idx in range(1,10): count_array[b_idx] += count_array[b_idx - 1]
        
        max_idx = list_size - 1
        while max_idx >= 0:
            index = random_number_list[max_idx] // exponent
            output[count_array[index % 10] - 1] = random_number_list[max_idx]
            count_array[index % 10] -= 1
            max_idx -= 1
        
        for c_idx in range(0, len(random_number_list)): random_number_list[c_idx] = output[c_idx]
        exponent *=10
    return random_number_list

def quick_sort(random_number_list: list) -> list:
    """
    PURPOSE: Sort the provided list using the quick sort algorithm
    ARGUMENT: random_number_list (list): the list to be sorted
    RETURN: (list): the sorted list
    """
    stack = [(0, len(random_number_list) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = quick_sort_partition(random_number_list, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    return random_number_list

def quick_sort_partition(random_number_list: list, low: int, high: int) -> int:
    """
    PURPOSE: Sort the random_number_list around it's pivot
    ARGUMENT: random_number_list (list): list being sorted, low (int): lowest element in list, high (int): highest element in list
    RETURN: (int) the index of the pivot + 1
    """
    pivot = random_number_list[high]
    i = low - 1
    for j in range(low, high):
        if random_number_list[j] <= pivot:
            i += 1
            random_number_list[i], random_number_list[j] = random_number_list[j], random_number_list[i]
    random_number_list[i + 1], random_number_list[high] = random_number_list[high], random_number_list[i + 1]
    return i + 1