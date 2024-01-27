from sortedcontainers import SortedSet
T = int(input())
for _ in range(T):
    s = SortedSet()
    for _ in range(int(input())):
        order, num = input().split()
        num = int(num)
        if order == 'I':
            s.add(num)
        elif order == 'D' and num == 1:
            if len(s) != 0 : s.remove(s[-1])
        elif order =='D' and num == -1:
            if len(s) != 0 : s.remove(s[0])
        
    if len(s) == 0 : print('EMPTY')
    else : print(s[-1], s[0])