

def Username():
    Username = input('Username: ')
    return Username
def Password():
    Password = input('Password: ')
    return Password

i = 0
Remaining = 5
while(i<=5):
    sys_username = 'Herakles'
    sys_password = '29501930'

user_entered = Username()
password_entered = Password()

if (sys_username == user_entered) and (sys_password == password_entered):
    print('Giriş Başarılı')

else:
    Remaining -= 1
    print('Wrong Username or Password')

if Remaining == 0:
    print('You are out of System Entry')
    
    i+= 1
