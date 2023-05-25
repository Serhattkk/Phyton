
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('0 sayısı kullanılamaz')
# except ValueError:
#     print('Harf kullanılamaz')



# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError, ValueError:
#     print('Hatalı yazım')


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('Hatalı yazım')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('Hatalı yazım', ex)
    else:
        break