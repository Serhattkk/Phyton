from time import sleep
import math

while True:
    def topla(num1,num2):
        print("İşlem Başlıyor...")
        sleep(1)
        result = num1 + num2
        print(f"Sonuç: {result}")
        
        
    def cikar(num1,num2):
        print("İşlem Başlıyor...")
        sleep(1)
        result = num1 - num2
        print(f"Sonuç: {result}")

    def carp(num1,num2):
        print("İşlem Başlıyor...")
        sleep(1)
        result = num1 * num2
        print(f"Sonuç: {result}")

    def bol(num1,num2):
        print("İşlem Başlıyor...")
        sleep(1)
        result = num1/num2
        print(f"Sonuç: {result}")
        
    def usal(num1,us):
        print("İşlem Başlıyor...")
        sleep(1)
        result = math.pow(num1,us)
        print(f"Sonuç: {result}")

    def karekok(num1):
        print("İşlem Başlıyor...")
        sleep(1)
        result = math.sqrt(num1)
        print(f"Sonuç: {result}")

    def faktoryel(num1):
        print("İşlem Başlıyor...")
        sleep(1)
        result = math.factorial(num1)
        print(f"Sonuç: {result}")


    print("1) Toplama\n2) Çıkarma\n3) Çarpma\n4) Bölme\n5) Üs Alma\n6) Karekök\n7) Çıkış\n")
    giris = input("Seçim: ")


    if (giris == "1"):
        num1 = int(input("1. Sayı:"))
        num2 = int(input("2. Sayı:"))
        topla(num1, num2)
    elif (giris == "2"):
        num1 = int(input("1. Sayı:"))
        num2 = int(input("2. Sayı:"))
        cikar(num1,num2)
    elif (giris == "3"):
        num1 = int(input("1. Sayı:"))
        num2 = int(input("2. Sayı:"))
        carp(num1,num2)
    elif (giris == "4"):
        num1 = int(input("1. Sayı:"))
        num2 = int(input("2. Sayı:"))
        bol(num1,num2)
    elif (giris == "5"):
        num1 = int(input("1. Sayı:"))
        us = int(input("Üs:"))
        usal(num1,us)
    elif (giris == "6"):
        num1 = int(input("1. Sayı:"))
        karekok(num1)
    elif (giris == "7"):
        break
    else:
        raise Exception("Geçersiz Giriş Değeri!")