import time

def get_list_of_numbers(size: int) -> list[int]:
    """
    PURPOSE: Create a list of values to count to of size (int)\n
    ARGUMENT: size (int)\n
    RETURN: (list): a list of values to count to of size (int)\n
    """
    return [1_000_000] * size

def count(number) -> str:
    """
    PURPOSE: Count to the number (int)\n
    ARGUMENT: number (int)\n
    RETURN: (str): the final value of the counter\n
    """
    counter = 0
    for i in range(number): counter += 1
    return f"{counter:,}"

def get_time_counter() -> float:
    """
    PURPOSE: Get a float representing the current time\n
    ARGUMENT: None\n
    RETURN: (float): representation of current time\n
    """
    return time.perf_counter()

def print_results(results: list[str], start: float, end: float) -> None:
    """
    PURPOSE: Print the final results\n
    ARGUMENT: result (list), start (float), end (float)\n
    RETURN: None\n
    """
    print(results)
    print(f"Time to complete {end - start}")