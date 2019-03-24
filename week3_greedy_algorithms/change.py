# Uses python3
import sys

def get_change(m):
    coins = (10, 5, 1)
    result = 0
    for coin in coins:
        temp = m // coin
        result += temp
        m = m - coin * temp
    return result

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
