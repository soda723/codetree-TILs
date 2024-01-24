n = int(input())
dots = [
    list(map(int, input().split())) for _ in range(n)
]

checkdict = {}
for dot in dots:
    if dot[0] in checkdict:
        if dot[1] < checkdict[dot[0]] :
            checkdict[dot[0]] = dot[1]
    else:
        checkdict[dot[0]] = dot[1]
s = 0
#print(checkdict)
for v in checkdict.values():
    s += v

print(s)