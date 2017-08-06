class Robot:
    '''## Robot class'''
    population = 0

    def __init__(self, name='Robot', price=10):
        '''# Init new robot (name, price)'''
        self.name = name
        self.price = price
        print('... Init-{0} [{1}] '.format(self.name, self.price))
        Robot.population += 1
        print('... population-{0} '.format(Robot.population))

    def __del__(self):
        '''# Delete robot '''
        print('   {0}-delete'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} deleted ok!'.format(self.name))
        else:
            print('Robot work: {0}'.format(Robot.population))

    def sayHi(self):
        '''# Print robote name'''
        print('Hello I\'m {0}'.format(self.name))

    @staticmethod
    def howMany():
        '''# Count robots'''
        print('We have: {0:d} robots'.format(Robot.population))

#
d1 = Robot()
d2 = Robot('R2-D1', 120)
d3 = Robot('C-3PO', 324)
Robot.howMany()

d1.sayHi()

print(Robot.__doc__)
print(Robot.sayHi.__doc__)