# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci(n):
    if n <= 1:
        return n
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

def find_pisano_period(m):
    previous = 0
    current = 1
    temp1 = current
    temp2 = previous + current
    n = 1
    while True:
        if (previous, current) == (temp1 % m, temp2 % m):
            return n
        else:
            temp1, temp2 = temp2, temp1 + temp2
        n += 1

def get_fibonacci_huge(n, m):
    pisano = find_pisano_period(m)
    fibo_number = n % pisano
    return fibonacci(fibo_number) % m



if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
