n = int(input())

grid =[
    list(map(int, input().split())) for _ in range(n)
]

paylist = sorted(grid, key = lambda x: x[2], reverse = True)
# endlist = sorted(grid, key = lambda x: x[1], reverse = True)
# ends = endlist[0][1]
# days = [0] * (ends +1)
days = []
#print(paylist)
answer = 0
for s, e, p in paylist:
    check = True
    for ds, de in days:
        if de >= s and ds <= e : 
            check = False
            break

    if check:
        answer += p
        days.append((s, e))
    
print(answer)