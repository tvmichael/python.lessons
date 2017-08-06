class Person:
    def __init__(self, name='Mik'):
        self.name = name
    def sayHi(self):
        print("Hello! Person : ", self.name)

p = Person()
p.sayHi()
print(p)

