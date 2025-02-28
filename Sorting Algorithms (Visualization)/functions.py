import random
import matplotlib.pyplot as plot

def get_random_number_list(size: int) -> list[int]:
    """
    PURPOSE: Create a list of random numbers\n
    ARGUMENT: size (int): The size of the desired list\n
    RETURN: (list): a list of random numbers\n
    """
    return [random.randint(a=0, b=1_000_000) for i in range(size)]

def show_sorting(idx: int, algorithm: str, list_of_numbers: list[int]) -> None:
    """
    PURPOSE: Display the sorting algorithm process\n
    ARGUMENT: idx: the index of the number that was swapped, algorithm: the name of the sorting algorithm, list_of_numbers: the list of numbers being sorted\n
    RETURN: None\n
    """
    plot.title(algorithm + f"{len(list_of_numbers):,}")
    plot.bar(range(len(list_of_numbers)), list_of_numbers, color=["black" if i not in idx else "red" for i in range(len(list_of_numbers))])
    plot.pause(.001)
    plot.clf()

def validate_sorting(algorithm: str, list_of_numbers: list[int]) -> None:
    """
    PURPOSE: Validate the sorting algorithm results\n
    ARGUMENT: algorithm: the name of the sorting algorithm, list_of_numbers: the list of numbers being sorted\n
    RETURN: None\n
    """
    plot.figure().canvas.manager.full_screen_toggle()
    plot.title(algorithm + f"{len(list_of_numbers):,}")
    plot.bar(range(len(list_of_numbers)), list_of_numbers, color=["green" if list_of_numbers[i] <= list_of_numbers[i + 1] else "red" for i in range(len(list_of_numbers) - 1)])
    plot.pause(1)
    plot.clf()

