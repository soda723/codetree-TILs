n, c, g, h = map(int, input().split())
dev = []
count = {}
for _ in range(n):
    a, b = map(int, input().split())
    dev.append([a,b])
    for num in range(a, b+1):
        if num in count : count[num] += 1
        else : count[num] = 1

temp = list(dict(sorted(count.items(), key=lambda x: x[1])).keys())[-1]

answer = 0
for ta, tb in dev:
    if temp < ta : answer += c
    elif temp > tb : answer += h
    else : answer += g

print(answer)