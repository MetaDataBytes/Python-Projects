from functions import factor_finder, print_factors

if __name__ == "__main__":
    num = 1_000_000
    factors = [i for i in factor_finder(num=num)]
    print_factors(factors=factors)