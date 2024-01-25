n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

listcheck = set(list1)
for v in list2:
    if v in listcheck: print(1, end=' ')
    else: print(0, end=' ')