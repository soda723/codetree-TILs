n, g = map(int, input().split())
groups = [
    list(map(int, input().split())) for _ in range(g)
]

invite = [0] * (n+1)
invite[1] = 1
while True:
    checkinvite = invite.count(1)
    for gr in groups:
        np = gr[0]
        HowManyInvite = 0
        for person in gr[1:np+1]:
            if invite[person] == 1 : HowManyInvite += 1
        
        if HowManyInvite + 1 >= np : 
            for person in gr[1:np+1]:
                invite[person] = 1

    if checkinvite == invite.count(1): break

print(checkinvite)