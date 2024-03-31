def maxinja(n, m):
    answer = 1
    for i in range(n, 1, -1):
        if n % i == 0 :
            if m % i == 0 :
                answer = i
                break
    print(answer)

n, m = map(int, input().split())
maxinja(n, m)