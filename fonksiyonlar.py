from lib2to3.pgen2.token import NAME
import string
from tkinter import S
from tokenize import Name
from unicodedata import name
from unittest import result

'''


def SayHello(name):
    return 'Hello ' + name


SayHello(input('name:'))
if (name == ' ' )or( name == ''):
        name == 'User'
else:
        name = name

'''
'''
def joı( name = 'user' ):
        return 'hello '+name

name = input('name: ')

if (name == ' ') or (name == ''):
        name == joı
else:
        name = name
msg = joı(name)

print(msg)

'''

'''
def number(num1, num2):
        return num1 + num2

num1 = int(input('num1: '))
num2 = int(input('num2: '))


total =(num1+num2)

print(total)

'''
'''
def yashesap(dyear):
        bugun = datetime.datetime.now()
        yas = bugun.year - dyear.year
        return yas



tarih = int(input('doğum yılınız: '))
print(yashesap(tarih))
'''
from datetime import datetime
def yasHesapla(dtarih):
  bugun = datetime.datetime.now()
  yas = bugun.year - dtarih.year - ((bugun.month, bugun.day) <(dtarih.month, dtarih.day))
  return yas
 
 
tarih = datetime.datetime(2022, 9, 13)
print(yasHesapla(tarih))
