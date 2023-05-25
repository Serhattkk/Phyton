fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0])    indekslenemez

for x in fruits: 
    print(x)

fruits.add('cheryy')
fruits.update(['mango', 'grape'])
print(fruits)

# mylist = [1,2,4,6,1,6,4]

# print(set(mylist))

fruits.remove('orange')
fruits.discard('apple')     #   ikiside listeden silmeye yarıyor

print(fruits)

fruits.pop()

fruits.clear()   #herşeyi siler