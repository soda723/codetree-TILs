from sortedcontainers import SortedSet
n = int(input())
nums = SortedSet([0])
order = list(map(int, input().split()))
mins = max(order)

for num in order:
    nums.add(num) # [0,3]
    check_idx = nums.bisect_right(num) # num보다 바로 큰 수 idx
    check_idx2 = nums.bisect_left(num)-1 # num 보다 바로 작은 수 idx

    if 0<= check_idx < len(nums) : diff = abs(num - nums[check_idx])
    else: diff = max(nums)

    if 0<= check_idx2 < len(nums) : diff2 = abs(num - nums[check_idx2])
    else: diff2 = max(nums)
    
    mins = min(mins, diff, diff2)

    print(mins)