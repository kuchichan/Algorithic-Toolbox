#Uses python3

import sys

def lcs2(a, b):
    n = len(a)
    m = len(b)
    D =[[None for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                D[0][j] = 0
            elif j == 0:
                D[i][0] = 0

    for j in range(1,m+1):
        for i in range(1, n+1):
            if a[i-1] == b[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
    return D[n][m]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
