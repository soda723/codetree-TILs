from sortedcontainers import SortedDict
n = int(input())
nums = list(map(int, input().split()))
sd = SortedDict()

for i, v in enumerate(nums):
    if v not in sd :
        sd[v] = i+1
for k, v in sd.items():
    print(k, v)