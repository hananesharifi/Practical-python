angle1 ,angle2 ,angle3 = input().split()
n = int(angle1)
m = int(angle2)
p = int(angle3)

def isTriangle(n ,m ,p):
    if n == 0 or m == 0 or p == 0:
        return 'No'
    else:
        sum1 = n + m + p
        if sum1 == 180:
            return 'Yes'
        else:
            return 'No'
t = isTriangle(n ,m ,p)
print(t)