t = int(input())
dic1 = {}
for i in range(t):
    n = int(input())
    values = []
    for j in range(n):
        m = input()
        values.append(m)
    dic1[n] = values

def compressstrings(n ,values):
    str1 = values[0]
    for i in range(1 ,n):
        if str1[-1] == values[i][0]:
            str1 += values[i][1:]
        else:
            str1 += values[i]
    return len(str1)

for i in dic1:
    c = compressstrings(i ,dic1[i])
    print(c))