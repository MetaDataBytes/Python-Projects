import random
import time
import string

def get_random_number_list(size: int) -> list[int]:
    """
    PURPOSE: Create a list of random numbers
    ARGUMENT: size (int): The size of the desired list
    RETURN: (list): a list of random numbers
    """
    return [random.randint(a=0, b=1_000_000) for i in range(size)]

def get_random_string_list(size: int) -> list[str]:
    """
    PURPOSE: Create a list of random string values
    ARGUMENT: size (int): The size of the desired list
    RETURN: (list): a list of random string values
    """
    return [random.choice(string.ascii_letters) for i in range(size)]

def get_time_counter() -> float:
    """
    PURPOSE: get a float representation for calculating duration
    ARGUMENT: None
    RETURN: (float): time representation for calculating duration
    """
    return time.perf_counter()

def print_number_list(number_list: list) -> None:
    """
    PURPOSE: Print the provided list of numbers
    ARGUMENT: number list (list): a list of numbers
    RETURN: None
    """
    print(' | '.join([f"{number:,}" for number in number_list]))

def test_sorted_order(list: list) -> bool:
    """
    PURPOSE: test if the provided list is sorted
    ARGUMENT: list (list): The list to be tested
    RETURN: (bool): True = sorted, False = unsorted
    """
    for i in range(len(list) - 1): 
        if list[i] > list[i + 1]: return False
    return True