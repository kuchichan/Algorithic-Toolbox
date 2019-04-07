#Uses python3

import sys

def lcs3(a, b, c):
    # it is nearly the same as in for 2 sequences
    n = len(a)
    m = len(b)
    L = len(c)
    D =[[[None for j in range(L+1)]
        for i in range(m+1)] for k in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            for k in range(L+1):
                # improvement :)
                if i == 0 or j == 0 or k == 0:
                    D[i][j][k] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, L+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])
    return D[n][m][L]


   #write your code here
    return min(len(a), len(b), len(c))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
