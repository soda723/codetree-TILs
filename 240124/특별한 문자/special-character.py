from collections import defaultdict
str1 = input()
count = defaultdict(lambda : 0)
for s in str1:
    count[s] += 1

check = False
for k in count.keys():
    if count[k] == 1 : 
        check = True
        break

if check : print(k)
else: print("None")