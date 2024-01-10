n = int(input())
temp = [0] * (n+2)
temp[1] = 1
temp[2] = 2
for i in range(3, n+1):
    temp[i] = temp[i-1] + temp[i-2]

print(temp[n]%10007)