n, s = map(int, input().split())
numbers = list(map(int, input().split()))
ans = n
j = 0
tsum = 0

for i in range(n):
    while i<=j<n and tsum + numbers[j] >= s:
        tsum += numbers[j] #
        j += 1 
        
    if tsum + numbers[j] < s : 
        j += 1
        tsum+= numbers[j]

    if i<=j<n:
        ans = min(ans, j-i+1)
        tsum -= numbers[i]
            
print(ans)