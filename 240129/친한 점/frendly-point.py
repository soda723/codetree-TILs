from sortedcontainers import SortedSet
n, m = map(int, input().split())
ss = SortedSet()

for _ in range(n) :
    x, y = map(int,input().split())
    ss.add((x,y))
    
for _ in range(m) :
    x, y = map(int,input().split())
    idx = ss.bisect_left((x, y))
    if 0<= idx < n:
        print("%d %d" % ss[idx])
    else: print(-1,-1)