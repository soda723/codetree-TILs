from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = SortedSet(map(int, input().split()))

for _ in range(m):
    num = int(input())
    idx = arr.bisect_left(num)
    if idx in range(n): print(arr[idx])
    else : print(-1)