# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def lcm(a, b):
    #calculate greatest common divisor
    c, d = a, b
    while d != 0:
        c, d = d, c % d

    return a * b // c
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

