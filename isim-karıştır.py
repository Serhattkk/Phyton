
import random

def generate_name():
    first_names = ["Serhat", "Merve", "Damla","Ali", "Gamze", "Arif"]
    last_names = ["Kayır", "Turgut", "Türkecan", "Altıok", 'Akşit', "Çetinkaya"]
    return "{} {}".format(random.choice(first_names), random.choice(last_names))

for i in range(6):
    print(generate_name())





