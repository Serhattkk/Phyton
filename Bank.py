def __init__(self,username,password):
    self.username = username
    self.password = password
    print('hazır')
sec = input('hesabınız var mı?: ')
if sec == "evet":
    sys_user = 'serhatkayir'
    sys_password = '2950'
    def oturum_ac(self):
        user = input('kullanıcı adı?: ')
        password = input('Şifre?: ')
        if sys_user == user and sys_password == password:
            print('Giriş başarılı')
            bakiye = 8648
            print("""
                    Para Yatır > 1
                    Para Çek > 2
                    Çık > 3
            """)
            ısec = input('Seçiminiz: ')
            if ısec == "1":
                ymiktar = input('Yatırma miktarı: ')
                print(f'{ymiktar}TL hesabınıza yatırlmıştır, yeni bakiyeniz: {ymiktar + bakiye}TL dir.')
            elif ısec == "2":
                cmiktar = input('Çekme miktarı: ')
                if cmiktar > bakiye:
                    print('Yetersiz bakiye')
                else:
                    print(f'{cmiktar}TL hesabınızdan çekilmiştir, kalan bakiyeniz: {bakiye + cmiktar}TL dir.')
            else:
                pass
