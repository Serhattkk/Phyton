import math

print("""

CALCULATOR

1 for total
2 for removal
3 for impact
4 for compartment
5 for square root
6 for square of
""")

islem = (input("Select Operation: "))


if islem == "1":
    print('total')
elif islem == "2":
    print('removal')
elif islem == "3":
    print('impact')
elif islem == "4":
    print('compartment')
elif islem == "5":
    print('square root')
else:
    print('squre of')

if islem == "5":
    num1 = int(input('Base: '))
    num2 = int(input('Base up: '))
elif islem == "6":
    num1 = int(input('Number 1: '))
else:
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))

if islem == "1":
    print("Result:", num1 + num2)
elif islem == "2":
    print("Result:", num1 - num2)
elif islem == "3":
    print("Result:", num1 * num2)
elif islem == "4":
    print("Result:", num1 / num2)
elif islem == "5":
    print("Result:",pow(num1, num2))
elif islem == "6":
    print(math.sqrt(num1))
else:
    print('Fail...')



