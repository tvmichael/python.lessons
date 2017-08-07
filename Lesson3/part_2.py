# STRING
print('-- STRING ----------------------- ')
message = "Hellou Python"
print(message)

#
s1 = "this is string 1"
s2 = "This is string TWO"
print(s1.title())
print(s2.lower())
print(s1.capitalize())
print(s1.upper())

#
s3 = s1 + '. ' + s2
print(s3)
print('\t' + s3)

#
s4 = '   Big  string with      many space  .   '
print('(' + s4.rstrip() + ')')
print('(' + s4.strip() + ')')


#NUMBER
print('-- NUMBER ----------------------- ')
n1 = 6
n2 = 1,3,4
n3 = n1 * n2
print(n3)

n1 = 6
n2 = 3.3
n3 = n1 * n2
print(n3)

# convert to string
age = 38
message = "Your age = " + str(age) + ' year'
print(message)