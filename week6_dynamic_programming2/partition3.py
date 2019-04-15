# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0
def partition_dyn(A):
    souv_sum = sum(A) // 3
    n = len(A)
    bool_table = [[([False] * (n+1))[:] for _ in range(souv_sum+1)] for _ in range(souv_sum+1)]
    # if sum == 0 then is always True
    bool_table[0][0][0] = True

    if n < 3 or (sum(A) % 3) or max(A) > souv_sum:
        return 0

    for i in range(1, n+1):
        v = A[i - 1]
        for j in range(souv_sum + 1):
            r1 = j - v
            for k in range(souv_sum +1):
                r2 = k - v
                if j == 0 and k == 0:
                    bool_table[0][0][i] = True
                elif v == j and any(bool_table[x][k][i-1] for x in range(souv_sum+1)):
                    bool_table[j][k][i] = True
                elif v == k and any(bool_table[j][x][i-1] for x in range(souv_sum+1)):
                    bool_table[j][k][i] = True
                elif bool_table[j][k][i-1]:
                    bool_table[j][k][i] = True
                elif r1 > 0 and bool_table[r1][k][i-1]:
                    bool_table[j][k][i] = True
                elif r2 > 0 and bool_table[j][r2][i-1]:
                    bool_table[j][k][i] = True

    return int(bool_table[souv_sum][souv_sum][n])

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition_dyn(A))

