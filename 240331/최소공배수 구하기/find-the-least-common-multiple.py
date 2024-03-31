n, m = map(int, input().split())

for i in range(2, m):
    if n*i % m == 0 : 
        print(n*i)
        break