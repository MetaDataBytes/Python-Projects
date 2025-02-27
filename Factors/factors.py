from functions import get_factor_pairs_list, print_factors

if __name__ == "__main__":
    num = 1_000_000_000_000_000
    factors = [i for i in get_factor_pairs_list(num=num)]
    print_factors(factors=factors)