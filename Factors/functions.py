from math import sqrt, ceil
import time

def get_time_counter() -> float:
    """
    PURPOSE: Get a counter for measuring duration\n
    ARGUMENT: None\n
    RETURN: a counter for determining duration\n
    """
    return time.perf_counter()

def get_factor_pairs_list(num: int) -> tuple[tuple[int]]:
    """
    PURPOSE: Find all the factor pairs for the provided number\n
    ARGUMENT: num (int): The number to find factor pairs for\n
    RETURN: A list of factor pairs for the provided number\n
    """
    return ((i, num // i) for i in range(1, ceil(sqrt(num))) if num % i == 0)

def print_factors(factors: list) -> None:
    """
    PURPOSE: print the provided factor pairs\n
    ARGUMENT: factors: the list of factor pairs\n
    RETURN: None\n
    """
    for i, factor_pair in enumerate(factors): print(f"{i + 1}. {factor_pair[0]:,} * {factor_pair[1]:,} = {factor_pair[0] * factor_pair[1]:,}")