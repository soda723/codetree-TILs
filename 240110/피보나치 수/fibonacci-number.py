n = int(input())
pivot = [-1, 1, 1]
for i in range(3, n):
    pivot.append(pivot[i-2]+pivot[i-1])
print(pivot[n])