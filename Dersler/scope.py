'''

x = 'Global'

def fun():
    # fonksiyon içindeki maddeler dıştaki maddeler ile bağımsızdır
    # dışarda x = global olmasına rağman içerdeki locala dokunmadı
    x = 'local'
    print(x)

fun()
print(x)
'''
###################
'''
name = 'Serhat'

def changename(new):
    name=new
    
    print(name)
    
changename('Merve')
print(name)

'''
#################

#################

name = 'global string'

def greeting():
    name = 'Eylül'
    
    def hello():
        print('Merhaba '+ name )
        
    hello()

greeting()

#################



