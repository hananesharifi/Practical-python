def isprime2(n):
    if n > 1:
        i = 2
        while i < n:
            if n % i == 0:
                print(n , 'is not prime!!')
                break
            i += 1
        else:
            print(n , 'is prime')   
    else:
        print(n , 'is not prime!!!')  
n = eval(input('please enter your number: '))
isprime2(n)