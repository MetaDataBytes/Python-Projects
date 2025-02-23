import time
import random
import string

def get_time_counter() -> float:
    """
    PURPOSE: get a float representation for calculating duration\n
    ARGUMENT: None\n
    RETURN: (float): time representation for calculating duration\n
    """
    return time.perf_counter()

def get_number_list(size: int) -> list[int]:
    """
    PURPOSE: Create a list of random numbers\n
    ARGUMENT: size (int): The size of the desired list\n
    RETURN: (list): a list of random numbers\n
    """
    return [random.randint(0, size) for i in range(size)]

def get_string_list(size: int) -> list[str]:
    """
    PURPOSE: Create a list of random strings\n
    ARGUMENT: size (int): The size of the desired list\n
    RETURN: (list): a list of random strings\n
    """
    return [random.choice(string.ascii_letters) for i in range(size)]

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
    return randomized_list

def quick_sort_partition(randomized_list: list, low: int, high: int) -> int:
    """
    PURPOSE: Sort the random_number_list around it's pivot\n
    ARGUMENT: random_number_list (list): list being sorted, low (int): lowest element in list, high (int): highest element in list\n
    RETURN: (int) the index of the pivot + 1\n
    """
    pivot = randomized_list[high]
    i = low - 1
    for j in range(low, high):
        if randomized_list[j] <= pivot:
            i += 1
            randomized_list[i], randomized_list[j] = randomized_list[j], randomized_list[i]
    randomized_list[i + 1], randomized_list[high] = randomized_list[high], randomized_list[i + 1]
    return i + 1

def print_number_list(number_list: list) -> None:
    """
    PURPOSE: Print the provided list of numbers\n
    ARGUMENT: number list (list): a list of numbers\n
    RETURN: None\n
    """
    print(' | '.join([f"{number:,}" for number in number_list]))

def test_found_value(search_list: list[any], search_value: any, index: int) -> bool:
    """
    PURPOSE: test if the provided index returns the search value\n
    ARGUMENT: list (list): The list that was searched, search_value (any): the value searched for, index (int): the location of the searched value\n
    RETURN: (bool): True = index points to search_value, False = index does not point to search value\n
    """
    if index == -1: return bool(search_value not in search_list)
    else: return bool(search_value == search_list[index])