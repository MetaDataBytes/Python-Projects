from functions import get_list_of_numbers, count
import multiprocessing

if __name__ == "__main__":
    numbers = get_list_of_numbers(int(input("Size of list: ")))
    results = multiprocessing.Pool().map(count, numbers)
    print(results)