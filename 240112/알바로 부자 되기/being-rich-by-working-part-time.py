n = int(input())
#[start, end, pay]
grid =[
    list(map(int, input().split())) for _ in range(n)
]
paylist = sorted(grid, key = lambda x: x[2], reverse = True)
endlist = sorted(grid, key = lambda x: x[1], reverse = True)
ends = endlist[0][1]
days = [0] * (ends +1)

#print(paylist)
answer = 0
for s, e, p in paylist:
    check = True
    for d in range(s, e+1):
        if days[d] == 1 : check = False

    if check:
        answer += p
        for d in range(s, e+1):
            days[d] = 1
    
print(answer)