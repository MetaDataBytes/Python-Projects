from functions import create_ulam_spiral, show_ulam_spiral

if __name__ == "__main__":
    """
    The Ulam spiral or prime spiral is a graphical depiction of the set of prime numbers, 
    devised by mathematician Stanisław Ulam in 1963. It is constructed by writing 
    the positive integers in a square spiral and specially marking the prime numbers.
    """
    primes = 25_000
    number_list, x, y = create_ulam_spiral(primes=primes)
    show_ulam_spiral(number_list=number_list, x=x, y=y)