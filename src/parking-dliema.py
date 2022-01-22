#!/bin/python3

import os


#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k

import sys
print(sys.path)


def carParkingRoof(cars, k):
    # Write your code here
    cars.sort()
    n = len(cars)
    res = float('inf')
    for i in range(n - k + 1):
        res = min(res, cars[i + k - 1] - cars[i])
    return res + 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cars_count = int(input().strip())

    cars = []

    for _ in range(cars_count):
        cars_item = int(input().strip())
        cars.append(cars_item)

    k = int(input().strip())

    result = carParkingRoof(cars, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
