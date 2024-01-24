from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()

for _ in range(n):
    color = input()
    if color in sd : sd[color] += 1
    else: sd[color] = 1

for k, v in sd.items():
    percent = v / n * 100
    print('%s %.4f'%(k, percent))