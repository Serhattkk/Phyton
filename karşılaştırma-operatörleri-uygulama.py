#girilen iki sayıdan hangisi büyük

# a = int(input('1.sayı'))

# b = int(input('2.sayı'))

# if a > b:
#     print('a b den büyüktür')

# elif b > a:
#     print('b a dan büyüktür')

# else: 
#     print('a ve b eşittir')

# #or

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# ortalama alma

# a = float(input('1.vize: '))
# b = float(input('2.vize: '))
# c = float(input('final: '))

# ort = (((a + b) / 2) * 0.6) + (c * 0.4)

#  print(f'not ortalamanız : {ort} ve dersten geçme durumunuz: {ort>=50}')  
# yada
# if ort>= 50:
#      print('pass')

#  else:
#      print('fail')

# tek mi çift mi anlama

# a = int(input('sayı: '))

# if(int(a)%2==0):
#       print("Sayı Çift")

# else:
#     print('sayı tek')

# sayı negatif mi pozitif mi

# sayi = input('sayı: ')

# if(int(sayi)>0):
#      print(sayi +" Sayısı Pozitif Sayıdır.")
# else:
#     print(sayi +" Sayısı Negatif Sayıdır.")

# parola ve mail doğruluğu

#(mail: kayir@kayir.com parola: abc07)

email: "kayir@kayir.com"
parola: "abc07"

girismail = input('mail: ')
girisparola = input('parola: ')

# if (girismail == email):
#     if(girisparola == parola):
#         print('giris basarılı')
#     else:
#         print('parola yanlış')
# else:
#     print('mail yanlış')

ismail = (email==girismail)
ispassword = (parola==girisparola)

print(f'Email doğrumu: {ismail} ve parola doğru mu:{ispassword}')