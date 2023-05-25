print("""
      Merhaba!
      
      Kullanıcı Hesabı seçiniz>
      
      Serhat > 1
      Ali Altıok > 2
      """)

secim = input('Hesap Seçiniz?: ')
if secim == "1":
    Serhat ={
        'Ad': 'Serhat Kayır',
        'Hesap No': '46669',
        'Bakiye': '8415',
        'Şifre': '3721'
    }
    print("""
          Bakiye sorgu> 1
          Para Çekme> 2
          """)
    komut = input('Seçiminiz?: ')
    if komut == "1":
        def bakiyeSorgu(hesap, bakiye):
            print(f"Merhaba {hesap['Ad']} hesabınızda {hesap['Bakiye']} TL tutarında bakiye bulunmaktadır.")
        bakiyeSorgu(Serhat, 'Bakiye')
    elif komut == "2":
        def paraCek(hesap, miktar):
            print(f"Merhaba {hesap['Ad']}")
            
            if (hesap['Bakiye']>= miktar):
                print('Paranız Hazır')
            else:
                print('Bakiye yetersiz...')
        cek = (input('Ne kadar Çekmek istiyorsunuz?: '))        
        paraCek(Serhat, cek )
    else:
        print('geçerisz') 
elif secim == "2":
    Ali ={
        'Ad': 'Serhat Kayır',
        'Hesap No': '46669',
        'Bakiye': '8415',
        'Şifre': '3721'
    }
    print("""
          Bakiye sorgu> 1
          Para Çekme> 2
          """)
    komut = input('Seçiminiz?: ')
    if komut == "1":
        def bakiyeSorgu(hesap, bakiye):
            print(f"Merhaba {hesap['Ad']} hesabınızda {hesap['Bakiye']} TL tutarında bakiye bulunmaktadır.")
        bakiyeSorgu(Ali, 'Bakiye')
    elif komut == "2":
        def paraCek(hesap, miktar):
            print(f"Merhaba {hesap['Ad']}")
            
            if (hesap['Bakiye']>= miktar):
                print('Paranız Hazır')
            else:
                print('Bakiye yetersiz...')
        cek = (input('Ne kadar Çekmek istiyorsunuz?: '))        
        paraCek(Ali, cek )
    else:
        print('geçerisz')
