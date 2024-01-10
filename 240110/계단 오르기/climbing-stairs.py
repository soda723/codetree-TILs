n = int(input())
temp = [0]*(n+2)
temp[0] = 0
temp[1] = 0
temp[2] = 1
temp[3] = 1
for i in range (4, n+1):
    temp[i] = temp[i-2] + temp[i-3]

#print(temp[0:10])
print(temp[n]%10007)