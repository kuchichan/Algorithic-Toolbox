# Uses python3
import sys
import collections

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    point_indices = collections.defaultdict(set)
    pairs = [(elem, 0) for elem in starts] + [(elem, 2) for elem in ends]

    for i, elem in enumerate(points):
        pairs.append((elem, 1))
        point_indices[elem].add(i)

    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))

    count = 0
    for elem, pointer in sorted_pairs:
        if pointer == 0:
            count += 1
        if pointer == 2:
            count -= 1
        if pointer == 1:
            for index in point_indices[elem]:
                cnt[index] = count

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
