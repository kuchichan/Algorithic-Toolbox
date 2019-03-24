# Uses python3
import sys

def optimal_summands(n):
    N = 1
    while (1 + N) * N / 2 <= n:
        N += 1
    k =  n  - ((1 + N - 1) * (N - 1)  // 2)
    summands = list(range(1, N - 1)) + [N - 1 + k]

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
