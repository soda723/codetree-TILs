from sortedcontainers import SortedSet
n, k = map(int, input().split())
nums = SortedSet(set(map(int, input().split())))
nums = nums[::-1]
for v in nums[:k]:
    print(v, end=' ')