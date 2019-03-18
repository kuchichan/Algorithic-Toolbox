# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def get_fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    # pisano period for mod 10
    pisano = 60

    # sum = F(n+2) - 1
    n = (n+2) % pisano

    for _ in range(n - 1):
        # no need to store entire number
        previous, current = current, (previous + current) % 10
    # some kind of hack if mod == 0
    return current - 1 if current != 0 else 9

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_sum(n))
