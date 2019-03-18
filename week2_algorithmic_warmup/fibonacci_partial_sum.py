# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def partial_fibonacci_sum(n, m):
    previous = 0
    current = 1
    # pisano period for mod 10
    pisano = 60

    # sum = F(n+2) - 1
    n = (n + 2) % pisano
    m = (m + 2) % pisano
    n1 = 0
    n2 = 0
    if n < m:
        n = n - 2
        m = m - 1
    else:
        n = n - 1
        m = m - 2
    for _ in range(n):
        # no need to store entire number
        previous, current = current, (previous + current)
    n1 = current

    previous = 0
    current = 1
    for _ in range(m):
        previous, current = current, (previous + current)
    n2 = current

    # some kind of hack if mod == 0
    return (n1 - n2) % 10 if n1 >= n2 else (n2 - n1) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(partial_fibonacci_sum(from_, to))
