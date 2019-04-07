# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    D =[[None for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                D[0][j] = j
            elif j == 0:
                D[i][0] = i

    for j in range(1,m+1):
        for i in range(1, n+1):
            ins = D[i][j-1] + 1
            dele = D[i-1][j] + 1
            mat = D[i-1][j-1]
            misma = D[i-1][j-1] + 1

            if s[i-1] == t[j-1]:
                D[i][j] = min(ins, dele, mat)
            else:
                D[i][j] = min(ins, dele, misma)
    return D[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
