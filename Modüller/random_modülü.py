import random
from xml.etree.ElementInclude import LimitedRecursiveIncludeError


# re = int(random.uniform(1,81)) # yada bunu yap random.randint(1,100)

names = ['ali','hakan','arif','serhat']

# re = names[random.randint(0,len(names)-1)] 
'yada'
re = random.choices(names)
print(re)

# liste = list(range(10))
# re = random.shuffle(liste)
# re = liste

# print(liste)

liste = range(100)
result = random.sample(liste,2)
result = re

print(re)
