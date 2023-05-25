import random

characters = 'qwertyuıopğüasdfghjklşizxcvbnmöç1234567890QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ'
special = '_-.,?!&'

number = input('Kaç adet istiyorsunuz?: ')
number = int(number)

length = input('Şifreniz uzunluğunuz?: ')
length = int(length)

special = input('Özel karakterler dahil edilsin mi? (Y/N): ')
special = (special)

for a in range(number):
    password = ""
if  special == "Y" and "y":
    for b in range ( length):
        password += random.choice(characters and special)
elif special == "N" and "n":
    for b in range ( length):
        password += random.choice(characters)
elif special != ("N" and "n" and "Y" and "y"):
    print('Şeçim yanlış yapıldığı için özel karakter dahil edilmeyecek.')
    for b in range ( length):
        password += random.choice(characters)
else:
    print('Şeçim yapılmadığı için özel karakter dahil edilmeyecek.')
    for b in range ( length):
        password += random.choice(characters)

print(f'Şifreniz Hazır \n {password}')
