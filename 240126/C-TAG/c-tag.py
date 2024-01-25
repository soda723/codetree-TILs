from itertools import combinations

n, m = map(int, input().split())
alist, blist = [], []
for _ in range(n):
    alist.append(input())

for _ in range(n):
    blist.append(input())

idx = range(1, m+1)
able = combinations(idx, 3)

answer=0
for i1, i2, i3 in able:
    aset, bset = set(), set()
    i1 -= 1 
    i2 -= 1
    i3 -= 1

    for aword in alist:
        aset.add(aword[i1]+aword[i2]+aword[i3])
    
    for bword in blist:
        bset.add(bword[i1]+bword[i2]+bword[i3]) 

    check = True
    for akey in aset:
        if akey in bset :
            check = False
            break

    if check : answer += 1

print(answer)