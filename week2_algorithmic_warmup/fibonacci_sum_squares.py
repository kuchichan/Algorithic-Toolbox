# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    # for mod 10
    pisano_period = 60
    n = n % pisano_period
    for _ in range(n):
        previous, current = current, (previous + current) % 10
    return (previous * current) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
