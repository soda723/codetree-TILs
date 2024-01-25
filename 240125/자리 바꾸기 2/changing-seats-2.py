n, k = map(int, input().split())

order = []
for _ in range(k):
    order.append(list(map(int, input().split())))

ori_chair = [x for x in range(n+1)]
chairs = [[] for _ in range(n+1)]

for _ in range(1):
    for idx, jdx in order:
        value_i = ori_chair[idx]
        value_j = ori_chair[jdx]
        chairs[value_i].append(jdx)
        chairs[value_j].append(idx)
        ori_chair[idx] = value_j
        ori_chair[jdx] = value_i
        print(chairs)
    
for idx in range(1,n+1):
    print(len(chairs[idx]))