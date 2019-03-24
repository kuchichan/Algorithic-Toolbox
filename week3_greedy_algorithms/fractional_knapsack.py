# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    loot_items = zip(weights, values)
    loot_items = sorted(loot_items, key=lambda x: x[1]/x[0], reverse=True)
    for weights, values in loot_items:
        if capacity <= 0:
            return value
        a = min(weights, capacity)
        value += a * values/weights
        weights -= a
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
