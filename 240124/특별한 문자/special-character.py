from collections import defaultdict
str1 = input()
count = defaultdict(lambda : 0)
for s in str1:
    count[s] += 1

tmp = dict(zip(count.values(), count.keys()))
print(tmp[1])