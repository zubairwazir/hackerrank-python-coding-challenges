#!/bin/python3

import os

import string


#
# Complete the 'simpleCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING encrypted
#  2. INTEGER k
#

def simpleCipher(encrypted, k):
    # Write your code here
    symbols_low = string.ascii_lowercase
    symbols_up = string.ascii_uppercase
    res = []
    for c in encrypted:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c) - k) % len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c) - k) % len(symbols_low)])
        else:
            res.append(c)

    return "".join(map(str, res))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    encrypted = input()

    k = int(input().strip())

    result = simpleCipher(encrypted, k)

    fptr.write(result + '\n')

    fptr.close()
