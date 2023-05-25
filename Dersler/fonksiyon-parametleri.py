
'''
def changeName(n):
    n = input('isim: ')

name = 'serhat'

changeName(name)

print(name) 
'''

'''
def change(n):
    n[1] = str(input('şehir: '))

sehirler = ['Denizli','Muğla']

n = sehirler[:]#slicing
change(sehirler)
print(sehirler)
print(n)
'''

# def add(*cash): # yıldız işareti olduğu için istedğin kadar parametre atarsın
#     return sum((cash))

# print(add(10,20,30))
# print(add(10,))
# print(add(10,20,30,60,40,10))

def displayname(**args):
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayname(name = 'Serhat', age = 15, city = 'Denizli', phone = '515454')
displayname(name = 'Merve', age = 16, city = 'Denizli', phone = '46466')

