n, s = map(int, input().split())
numbers = list(map(int, input().split()))
ans = n
for i in range(n):
    tmp_sum = 0
    for j in range(i, n):
        tmp_sum += numbers[j]
        if tmp_sum == s :
            if ans > j-i+1: ans = j-i+1
            break
        elif tmp_sum > s : break
            
print(ans)