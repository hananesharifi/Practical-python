n1 = eval(input())
n2 = eval(input())

def reverseNumber(n):
    n_str = str(n)
    re_str = n_str[::-1]
    re_n = int(re_str)
    return re_n
if reverseNumber(n1) > reverseNumber(n2):
    print(str(n2) + ' < ' + str(n1))
elif reverseNumber(n2) > reverseNumber(n1):
    print(str(n1) + ' < ' + str(n2))
else:
    print(str(n2) + ' = ' + str(n1))