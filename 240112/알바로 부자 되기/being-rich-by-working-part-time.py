n = int(input())

grid =[
    list(map(int, input().split())) for _ in range(n)
]

for idx in range(n):
    s, e, p = grid[idx]
    day = e-s +1
    priority = round(p / day, 2)
    grid[idx].append(day)
    grid[idx].append(priority)
    

paylist = sorted(grid, key=lambda x: (-x[-1], x[-2]))
# endlist = sorted(grid, key = lambda x: x[1], reverse = True)
# ends = endlist[0][1]
# days = [0] * (ends +1)

days = []
#print(paylist)
answer = 0
for s, e, p, _, _ in paylist:
    check = True
    for ds, de in days:
        if de >= s and ds <= e : 
            check = False
            break

    if check:
        answer += p
        days.append((s, e))
    
print(answer)