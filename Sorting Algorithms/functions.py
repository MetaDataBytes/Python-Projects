from typing import Union
import random
import time
import string

def get_random_number_list(size: int) -> list[int]:
    """
    PURPOSE: Create a list of random numbers\n
    ARGUMENT: size (int): The size of the desired list\n
    RETURN: (list): a list of random numbers\n
    """
    return [random.randint(a=0, b=1_000_000) for i in range(size)]

def get_random_string_list(size: int) -> list[str]:
    """
    PURPOSE: Create a list of random string values\n
    ARGUMENT: size (int): The size of the desired list\n
    RETURN: (list): a list of random string values\n
    """
    return [random.choice(string.ascii_letters) for i in range(size)]

def get_time_counter() -> float:
    """
    PURPOSE: get a float representation for calculating duration\n
    ARGUMENT: None\n
    RETURN: (float): time representation for calculating duration\n
    """
    return time.perf_counter()

def test_sorted_order(list: list[any]) -> bool:
    """
    PURPOSE: test if the provided list is sorted\n
    ARGUMENT: list (list): The list to be tested\n
    RETURN: (bool): True = sorted, False = unsorted\n
    """
    for i in range(len(list) - 1): 
        if list[i] > list[i + 1]: return False
    return True