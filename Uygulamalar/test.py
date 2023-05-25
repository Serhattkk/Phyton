Serhat ={
        'Ad': 'Serhat Kayır',
        'Hesap No': '46669',
        'Bakiye': '8415',
        'Şifre': '3721'
    }
    def paraYatır(hesap, bakiye):
        print(f"Merhaba {hesap['Ad']} hesabına başarılı bir şekilde {hesap['yatir']} TL yatırlımıştır yeni bakiyeniz {hesap['Bakiye']} dir.")
        
        yatir = (input('Ne kadar yatırmak istiyorsunuz?: ')) 
        paraYatır(Serhat, yatir)
