from sortedcontainers import SortedSet
n, m = map(int, input().split())
nums = SortedSet(list(range(1, m+1)))
order = list(map(int, input().split()))

for o in order:
    nums.remove(o)
    print(nums[-1])