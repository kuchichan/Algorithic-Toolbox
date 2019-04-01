#Uses python3
import sys
import math

def calc_dist(x, y):
    return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))

def brute_force_calc(P):
    result = calc_dist(P[0], P[1])
    N = len(P)
    if N == 2:
        return result
    for i in range(N -1):
        for j in range(i+1, N):
            if i !=0 and j !=1:
                c = calc_dist(P[i], P[j])
                if c < result:
                    result = c
    return result

def strip_points(Px, d):
    result = d
    N = len(Px)
    for i in range(N-1):
        j = i + 1
        while j < min(i + 7, N) and Px[j][1] - Px[i][1] < result:
            c = calc_dist(Px[i], Px[j])
            if c < result:
                result = c
            j += 1
    return result

def closest(Px, Py):
    if len(Px) <= 3:
        return brute_force_calc(Px)

    mid = len(Px) // 2
    midPoint = Px[mid][0]
    Pyl = list()
    Pyr = list()
    for elem in Py:
        if elem[0] <= midPoint:
            Pyl.append(elem)
        else:
            Pyr.append(elem)

    dl = closest(Px[:mid], Pyl)
    dr = closest(Px[mid:], Pyr)

    d = min(dl, dr)

    strip = [elem for elem in Py if
            abs(elem[0] - midPoint) < d]

    return min(d, strip_points(strip, d))



def minimum_distance(x, y):
    points = list(zip(x, y))
    Px = sorted(points, key= lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])

    return closest(Px, Py)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
