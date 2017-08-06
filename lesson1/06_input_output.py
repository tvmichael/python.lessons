#
s2 = '0123456789'

s22 = s2[7]
print(s22)
s22 = s2[3:7]
print(s22)
s22 = s2[3::2]
print(s22)
s22 = s2[::-2]
print(s22)

#
print()
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Input trxt: ')
if (is_palindrome(something)):
    print("Yes, palindrome")
else:
    print('No, it\'s not a polindrome')
