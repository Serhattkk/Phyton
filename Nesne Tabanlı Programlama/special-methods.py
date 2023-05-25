class Moive():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Moive ready')
        
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('Moive has been deleted')
m = Moive('Interstellar', 'Christopher Nolan', 169)

print(len(m))
print(len(Moive))

del m
print(m)