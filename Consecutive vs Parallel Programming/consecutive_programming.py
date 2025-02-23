from functions import get_list_of_numbers, get_time_counter, count, print_results

if __name__ == "__main__":
    numbers = get_list_of_numbers(int(input("Size of list: ")))
    start = get_time_counter()
    results = [count(number=number) for number in numbers]
    end = get_time_counter()
    print_results(results=results, start=start, end=end)