def draw1(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            x = '*'
            print(x * i , end = '')
            print()
n = eval(input('plesas enter a number: '))
draw(n)
---------------------------------------------------------------------------
def draw2(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            for j in range(i):
                x = '*'
                print(x , end='')
            print()
n = eval(input('plesas enter a number: '))
draw2(n)
-------------------------------------------------------------------------
def draw3(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            x = '*'
            print(' ' * (n - i) , x * i , end='')
            print()

n = eval(input('plesas enter a number: '))
draw3(n)
--------------------------------------------------------------------------
def draw4(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            for j in range(i , n):
                x = '*'
                print(' ' , end= '')
            for k in range(i):
                print(x , end= '')
            print()
n = eval(input('plesas enter a number: '))
draw4(n)
----------------------------------------------------------------------
def draw5(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            x = '*'
            print(x * (n - i) , ' ' * i , end= '')
            print()
n = eval(input('plesas enter a number: '))
draw5(n)
-----------------------------------------------------------------------
def draw6(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            for j in range(i , n):
                x = '*'
                print(x , end= '')
            print()
n = eval(input('plesas enter a number: '))
draw6(n)
-------------------------------------------------------------------
def draw7(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            x = '*'
            print(' ' * i , end= '')
            print(x * (n - i) )
            
n = eval(input('plesas enter a number: '))
draw7(n)
---------------------------------------------------------------------
def draw8(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            for j in range(i):
                print(' ' , end= '')
            for k in range(i , n):
                x = '*'
                print(x , end= '')
            print()
n = eval(input('plesas enter a number: '))
draw8(n)
---------------------------------------------------------------------------
def draw9(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            x = '*'
            print(' ' * (n - i) , x * (2 * i - 1) , end= '')
            print()
            
n = eval(input('plesas enter a number: '))
draw9(n)
------------------------------------------------------------------
def draw10(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            for j in range(i , n):
                print(' ' , end= '')
            for k in range(2 * i - 1):
                    x = '*'
                    print(x , end= '')
            print()
n = eval(input('plesas enter a number: '))
draw10(n)
-------------------------------------------------------------
def draw11(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            x = '*'
            print(' ' * (n - i) ,  x * (2 * i - 1) , end= '')
            print()
        for i in range(n - 2 , 0 , -1):
            print(' ' * (n - i) ,  x * (2 * i - 1) , end= '')
            print()
n = eval(input('plesas enter a number: '))
draw11(n)
-------------------------------------------------------------------
def draw12(n):
    if n <= 0:
        print('It is not valid value, plesas try again!!!')
    else:
        for i in range(n):
            for j in range(i , n):
                print(' ' , end= '')
            for k in range(2 * i - 1):
                x = '*'
                print(x , end= '')
            print()
        for i in range(n - 2 , 0 , -1):
            for j in range(i , n):
                print(' ' , end= '')
            for k in range(2 * i - 1):
                x = '*'
                print(x , end= '')
            print()
           
n = eval(input('plesas enter a number: '))
draw12(n)
----------------------------------------------------------------------
