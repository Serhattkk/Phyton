




print("""

Üçgen Şekli Hesaplama

Uzunluğa göre ise 1
Açısına göre ise 2

""")


while True:
    choice = (input("Seçiminiz?: "))


    if (choice == "1"):
        A = (input('A Kenarı: '))
        B = (input('B Kenarı: '))
        C = (input('C Kenarı: '))
        if A == B == C:
            print('Eşkenar Üçgen')
        elif (A == B > C) or (A == B < C) or (A == C > B) or (A == C < B) or (B == C > A) or (B == C < A):
            print('İkizkenar Üçgen ')
        else:
            print('Karma Üçgen')
    elif (choice == "2"):
        A = int(input('A Açısı: '))
        B = int(input('B Açısı: '))
        C = int(input('C Açısı: '))
        total = (int(A + B + C))
        if total == '180':
            if (A == '90') or (B == '90') or (C == '90'):
                print('Dik Açılı Üçgen')
            elif (A > "90") or (B > "90") or (C > "90"):
                print('Geniş Açılı Üçgen')
            else:
                print('Dar Açılı Üçgen')
        else:
            print('Üçgen Açı Toplamı Yetersiz veya Fazla... \n Açı Toplamı 180 olmalıdır.')
    else:
        print('Geçersiz İşlem Girdiniz')
