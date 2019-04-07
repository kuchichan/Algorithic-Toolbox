# Uses python3
import sys

def get_change(m):
    denominations = (1, 3, 4)
    results = {0: 0}
    if m == 0:
        return results[0]
    for i in range(1, m+1):
        min_num_coins = float('inf')
        for elem in denominations:
            if i >= elem:
                num_coins = results[i - elem] + 1
                if num_coins < min_num_coins:
                    min_num_coins = num_coins
                    results[i] = min_num_coins
    return results[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
