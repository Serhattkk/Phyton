import numbers
import re
from unittest import result


# def square(num): return num **2

# num = []
# num.append(result)


# result = square((input('sayı1: ')))

# result = square((input('sayı2: ')))

# result = square((input('sayı3: ')))



# for item in map(square, num):
#     print(item)


def square(num): return num ** 2 
numbers = []

i = 0

while(i<3):
    result = square(int(input('sayı: ')))
    i += 1
    numbers.append(result)


for item in map(square,numbers):
    print(item)