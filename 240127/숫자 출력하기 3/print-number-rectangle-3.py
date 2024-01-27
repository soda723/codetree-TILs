n, m = map(int, input().split())
max = n*m 
for x in range(n):
    for y in range(m):
        result = (x+1) + n*y
        print(result, end=' ')
    print()