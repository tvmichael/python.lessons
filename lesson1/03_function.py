# functions
def say_hello():
    print('-f-h-')
    for i in range(5):
        print(i)
    print('-f-h-')
say_hello()

def n_fun(nx):
    print('__________')
    print('-n-f->', nx)
    print('----------')
n_fun(111)
n_fun(222)

#local
x = 50
def fun_x(x):
    print('local x= ', x)
    x = 55
    print('local x= ', x)
fun_x(12)
print('x=', x)

#global
y = 150
def fun_y():
    global y
    print('y= ', y)
    y = 155
    print('y= ', y)
fun_y()
print('y=>', y)

#default
print('--------- default')
def fun_def(x, y = 11):
    print('sum=', x + y)
fun_def(7)
fun_def(7,7)

# nonlocal
print('---------- nonlocal')
q1 = 10
def fun_nonlocal():
    q = 11
    global q1
    print('>>> q=', q, ' q1=',q1)
    def f_inside():
        nonlocal q
        print('nonlocal= ', q)
        q = 12
        print('nonlocal= ', q)
        q1 = 13
        print('nonlocal= ', q1)
    f_inside()
    print('=== q=', q, ' q1=', q1)
    q1=14
fun_nonlocal()
print('q1=',q1)

#keyword
print('---------- keyword')
def fun_keyword(a, b=2, c=4, d=8):
    print('a=', a, '  b=', b, '  c=', c, '  d=',d)
fun_keyword(111, 222)
fun_keyword(111, c=222)
fun_keyword(111, d=222, b=333)
fun_keyword(a=444, d=222)

# vararg
print('---------- vararg')
n_var = (7, 2, 3)
def fun_vararg(a=5, *b, **c):
    print('a=', a, '  b=', b, '  c=', c)
    for i in b:
        print('single= ', i)
fun_vararg(n_var, n_var, n_var, 321, n_var, n_var, m_mik=543)

# key only
print('---------- key only')
def fun_keyonly(a=1, *b, c_p, d_p):
    print('a=', a, '  b=', b, '  cp=', c_p, '  dp=', d_p)
fun_keyonly(15, (3, 4, 5), c_p='c1', d_p='d1')

# return
print('---------- return')
def fun_return(a=1, *b):
    ''' Function documentation.
        1. number
        2. other number'''

    if a == 15:
        return '[ a ~ 15 ]'
    if a > 10:
        return '[ a > 10 ]'
    else:
        return '[ a = ' + str(a) + ' ]'
print('n11=')
n11 = int(input())
print(fun_return(n11))
print(fun_return.__doc__)

