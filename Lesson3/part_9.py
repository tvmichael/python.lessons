# class

class Dog():
    '''Simple dog model'''
    def __init__(self, name, age, weight = ''):
        self.name = name
        self.age = age
        self.breed = 'unknown'
        self.weight = weight

    def dog_sit(self):
        print('Sit - %s' % self.name)

    def dog_up(self):
        print('Up - {0}'.format(self.name))

#
my_dog = Dog('Gavchik', 11)
print(my_dog.name)
my_dog.dog_sit()
my_dog.dog_up()
#
print(my_dog.breed)
my_dog.breed = 'Terer'
print(my_dog.breed)


#
print('-- owner dog')
class PrivateDog(Dog):
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def show_owner(self):
        print("Owner: %s" % self.owner_name)


# class ...
print('\n-- class ...')
class Car():
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.odometer = 0

    def update_odometr(self, km):
        self.odometr += km

    def read_odometr(self):
        print('Odometr = ', self.odometer)

class Battery():
    def __init__(self, battary_size):
        self.battary_size = battary_size
        self.max_current = None

    def max_battary_current(self, curreant):
        self.max_current = curreant

    def descryb_battary(self):
        print('Batary:', self.battary_size)
        print('.max current: %s' % self.max_current)


class ElectricalCar(Car):
    def __init__(self, model, year):
        super().__init__(model, year)
        self.battary = Battery(2000)

    def car_info(self):
        print('INFO:')
        print('Model: %s' %self.model)
        print('Year: %s' % self.year)
        self.battary.descryb_battary()

elka = ElectricalCar('Yaguar', 2013)
elka.battary.descryb_battary()
elka.car_info();


# standart class
print('-- ')
from collections import OrderedDict
favorite_lenguages = OrderedDict()
favorite_lenguages['jen'] = 'python'
favorite_lenguages['ron'] = 'php'
favorite_lenguages['adam'] = 'css'
favorite_lenguages['jordg'] = 'ruby'

for name, language in favorite_lenguages.items():
    print('Name- {0}, leng:( {1} )'.format(name.title(), language))
favorite_lenguages.clear()