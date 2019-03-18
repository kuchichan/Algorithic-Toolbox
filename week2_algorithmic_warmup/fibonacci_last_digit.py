# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    # pisano period for modulo 10
    pisano_period = 60
    previous = 0
    current  = 1

    # sum F(n+2) -1
    fibo_number = (n + 2) % pisano_period

    for _ in range(fibo_number - 1):
        # no need to store entire number
        previous, current = current, (previous + current) % 10

    return current
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
