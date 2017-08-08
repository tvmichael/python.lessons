# function

#
def f1(*x):
    for i in x:
        print('= ', i)
    print()

f1(1,2,3,4,5)
f1('a', 'b')


#
print('--')
def build_f(first, last, *any_variable, **name_list):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    # *
    for i in any_variable:
        profile['c' + str(i)] = i
    # **
    for key, value in name_list.items():
        profile[key] = value
    #
    print(profile)

build_f('start', 'end', 12, 13, 14, 15, name='MIk', age='38')