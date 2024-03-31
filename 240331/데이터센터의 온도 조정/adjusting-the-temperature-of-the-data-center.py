n, c, g, h = map(int, input().split())
dev = []
minta = False
maxtb = False
for _ in range(n):
    a, b = map(int, input().split())
    if minta == False : minta = a
    else : 
        minta = min(minta, a)
        maxtb = max(maxtb, b)
    
    dev.append([a,b])

count = {}
for a, b in dev:
    for num in range(a, b+1):
        if num in count : count[num] += g
        else : count[num] = g

    for num in range(minta, a):
        if num in count : count[num] += c
        else : count[num] = c
    
    for num in range(b+1, maxtb+1):
        if num in count : count[num] += h
        else : count[num] = h


temp = list(dict(sorted(count.items(), key=lambda x: x[1])).values())[-1]


print(temp)