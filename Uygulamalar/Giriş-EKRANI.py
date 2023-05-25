

def Username():
    Username = input('Username: ')
def Password():
    Password = input('Password: ')

i = 0
Remaining = 3
while(i<=3):
    sys_username = 'Herakles'
    sys_password = '2950'

    user_entered = Username()
    password_entered = Password()

    if (sys_username == user_entered) and (sys_password == password_entered):
        print('Giriş Başarılı')
    else:
        Remaining -= 1
        print('Wrong Username or Password')
        print(Remaining)
        if Remaining == 0:
            print('You are out of System Entry')
        

    i+= 1
