#Uses python3

import sys
def is_greater_or_equal(a, b):
    return int(str(a)+str(b)) >= int(str(b)+str(a))



def largest_number(a):

    res = ''
    while a:
        max_digit = 0
        for digit in a:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        a.remove(max_digit)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

