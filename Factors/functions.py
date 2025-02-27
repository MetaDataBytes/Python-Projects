import time
from typing import Generator

def get_time_counter() -> float:
    """
    PURPOSE: Get a counter for measuring duration\n
    ARGUMENT: None\n
    RETURN: a counter for determining duration\n
    """
    return time.perf_counter()

def factor_finder(num: int) -> Generator[list[int], any, None]:
    """
    PURPOSE: Find all the factor pairs for the provided number\n
    ARGUMENT: num (int): The number to find factor pairs for\n
    RETURN: A factor pair for the provided number\n
    """
    i = 1
    while i * i <= num:
        if num % i == 0: yield [i, num // i]
        i += 1

def print_factors(factors: list) -> None:
    """
    PURPOSE: print the provided factor pairs\n
    ARGUMENT: factors: the list of factor pairs\n
    RETURN: None\n
    """
    for i, factor_pair in enumerate(factors): print(f"{i + 1}. {factor_pair[0]:,} * {factor_pair[1]:,} = {factor_pair[0] * factor_pair[1]:,}")