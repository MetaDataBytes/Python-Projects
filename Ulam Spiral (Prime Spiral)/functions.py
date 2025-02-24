from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle

def create_ulam_spiral(primes: int) -> tuple[list[bool], list[int], list[int]]:
    """
    PURPOSE: Calculate the primality and x,y coordinates for each number in the ulam spiral\n
    ARGUMENT: primes: The desired number of primes to search for\n
    RETURN: number_list: a list of primalities index represents number, x: list of x coordinates for each number, y: list of y coordinates for each number\n
    """
    number = 2
    number_list = [False] # 1 is not prime
    x, y = [0], [0]  # Store X, Y coordinates. 1 coordinates are (0,0)
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # X Y movement
    direction = 0 # index for dx, dy to determine direction to move in
    segment_length = 1 # how many numbers for current direction
    segment_counter = 0 # numbers in current direction
    
    while sum(number_list) < primes: # keep searching for primes until we find the desired amount
        number_list.append(is_prime(number=number)) # Get primality of current number
        x.append(x[-1] + dx[direction]) # add x coordinates for current number
        y.append(y[-1] + dy[direction]) # add y coordinates for current number
        segment_counter += 1 # increment segment_counter

        if segment_counter == segment_length: # if segment_counter equals segment_length change direction (rotate left 90 degrees)
            direction = (direction + 1) % 4 # change direction
            segment_counter = 0 # reset segment_counter
            if direction % 2 == 0: segment_length += 1 # increase segment_length by one for each half rotation (180 degrees)
        number += 1
    return number_list, x, y

def is_prime(number: int) -> bool:
    """
    PURPOSE: Test the provided number for primality\n
    ARGUMENT: number: The number to test for primality\n
    RETURN: True if the number is prime, False if the number is not prime\n
    """
    if number < 2: return False
    elif number < 4: return True
    elif number % 2 == 0 or number % 3 == 0: return False
    for i in range(5, int(sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0: return False
    return True

def show_ulam_spiral(number_list: list[bool], x: list[int], y: list[int]) -> None:
    """
    PURPOSE: plot the ulam spiral\n
    ARGUMENT: number_list: the list of prime and composite numbers, x: the x coordinates for the list of numbers, y: the y coordinates for the list of numbers\n
    RETURN: None\n
    """
    mplstyle.use('dark_background')
    plt.subplots_adjust(left=0, right=0.9, top=0.96, bottom=0, wspace=0, hspace=0)
    plt.axis('off')
    plt.axis('equal')
    plt.title(f"Ulam Spiral | Primes: {sum(number_list):,} | Composites: {len(number_list) - sum(number_list):,} | Total: {len(number_list):,}")
    plt.scatter(x, y, s=0.5, c=['red' if number_list[i] else 'black' for i, _ in enumerate(number_list)]) # change 'else' color to see composites
    plt.show()