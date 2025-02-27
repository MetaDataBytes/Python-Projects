from functions import get_list_of_numbers, count

if __name__ == "__main__":
    numbers = get_list_of_numbers(int(input("Size of list: ")))
    results = [count(number=number) for number in numbers]
    print(results)