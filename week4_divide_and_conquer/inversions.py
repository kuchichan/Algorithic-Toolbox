# Uses python3
import sys

def merge(a, b, left, ave, right):
    n1 = ave - left
    n2 = right - ave

    count = 0
    L = list()
    R = list()

    for i in range(n1):
        L.append(a[left + i])
    for j in range(n2):
        R.append(a[ave  +j])

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
            count += ave - (left +i)
        k += 1

    while i < n1:
        a[k] = L[i]
        k += 1
        i += 1
    while j < n2:
        a[k] = R[j]
        k += 1
        j += 1
    return count
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a,b, left, ave, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
