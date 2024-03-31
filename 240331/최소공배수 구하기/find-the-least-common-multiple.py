def sol(n, m) :
    for i in range(m, n*m+1):
        if i%n == 0 and i%m == 0 :
            answer = i
            break
    print(answer)
    
n, m = map(int, input().split())
sol(n, m)