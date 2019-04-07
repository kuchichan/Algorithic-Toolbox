# Uses python3
import sys

def optimal_sequence(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        # the preceding number + 1 OR maybe better...
        e = arr[i -1] +1
        if i % 2 == 0:
            e = min(e, arr[i//2] + 1)
        if i % 3 == 0:
            e = min(e, arr[i//3] + 1)

        arr.append(e)
    sequence = []
    i = n
    while i > 1:
        #just read arr and calculate itermediate step...
        sequence.append(i)
        if arr[i -1] == arr[i] -1:
            i -= 1
        elif i % 2 == 0 and arr[i//2] == arr[i] - 1:
            i //= 2
        elif i % 3 == 0 and arr[i//3] == arr[i] - 1:
            i //= 3
    sequence.append(1)

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
