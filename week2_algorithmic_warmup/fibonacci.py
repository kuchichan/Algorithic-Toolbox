# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_2(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input())
print(calc_fib_2(n))
