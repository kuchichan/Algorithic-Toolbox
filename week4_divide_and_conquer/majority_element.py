# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = left + (right - left) // 2

    r = get_majority_element(a, mid, right)
    L = get_majority_element(a, left, mid)
    if r == L:
        return r
    cr = 0
    cL = 0
    for i in range(left, right):
        if a[i] == r:
            cr += 1
        if a[i] == L:
            cL += 1
    if cL > (right - left) // 2:
        return L
    elif cr > (right - left) // 2:
        return r
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
