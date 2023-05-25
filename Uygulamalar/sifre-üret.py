import random

characters = 'qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ'
specials = '_-.,?!&'

numerals = '1234567890'
numerals = int(numerals)

number = input('Kaç adet istiyorsunuz?: ')
number = int(number)

length = input('Şifreniz uzunluğunuz?: ')
length = int(length)

special = input('Özel karakterler dahil edilsin mi? (Y/N): ')
special = (specials)

numeral = input('Rakamlar dahil edilsin mi? (Y/N): ')
numeral = (numerals)

for a in range((number)):
    password = ""   
if  special == "Y" and "y":
    if numeral == "Y" and "y":
        for b in range ( length):
            password += random.choice(characters) and random.choice(specials) and random.choice(numerals)
    else:
        for b in range ( length):
            password += random.choice(characters) and random.choice(specials)
elif special == "N" and "n":
    if numeral == "Y" and "y":
        for b in range ( length):
            password += random.choice(characters) and random.choice(numerals)
    else:
        for b in range ( length):
            password += random.choice(characters)
else:
    if numeral != "Y" or "y" or "N" or "n":
        print('Rakam şeçimi yanlış yapıldığı için dahil edilmeyecek!')
    elif special != "Y" or "y" or "N" or "n":
        print('Özel karakter seçimi yanlış yapıldığı için dahil edilmeyecek!')
    else:
        print('Şeçim yapılmadığı için  dahil edilmeyecek.')
        for b in range ( length):
            password += random.choice()
   

print(f'Şifreniz Hazır \n {password}')














# else:
#     print('Şeçim yapılmadığı için özel karakter dahil edilmeyecek.')
#     for b in range ( length):
#         password += random.choice(characters)
   