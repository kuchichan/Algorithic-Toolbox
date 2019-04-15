# Uses python3
import sys

def dynamic_knapsack(W, w):
    V = [[0 for elem in range(W + 1)] for elem in w]
    for i in range(W + 1):
        V[0][i] = 0
    for j, _ in enumerate(w):
        V[j][0] = 0

    for i, _ in enumerate(w):
        for j in range(1, W + 1):
            V[i][j] = V[i-1][j]
            if w[i] <= j:
                val = V[i - 1][j - w[i]] + w[i]
                if V[i][j] < val:
                    V[i][j] = val
    return V[len(w)-1][W]


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(dynamic_knapsack(W, w))
