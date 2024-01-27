from itertools import combinations

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arrplus = []
for a in arr:
    arrplus.append(a+1)

combi = combinations(range(N), L)
answer = -1
for c in combi:
    newarr = []
    for i in range(N) :
        if i in c : newarr.append(arrplus[i])
        else : newarr.append(arr[i])

    #print(c, newarr)

    newarr.sort()
    counts = {}
    for idx, h in enumerate(newarr):
        if h in counts : continue
        else: counts[h] = N - idx

    #print(counts)

    mini_answer = -1
    for k, v in counts.items():
        if k <= v : 
            mini_answer = max(mini_answer, k)

    #print(mini_answer)

    answer = max(mini_answer, answer)
    #print(answer)

print(answer)