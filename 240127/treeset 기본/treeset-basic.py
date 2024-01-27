from sortedcontainers import SortedSet

# s = SortedSet() # 오름차순정렬, 균형이진트리
# s.bisect_left(E) # E보다 같거나 큰 최초의 데이터의 indx
# s.bisect_right(E)# E보다 큰 최초의 데이터의 indx

n = int(input())
ss = SortedSet()
for idx in range(n):
    order = list(input().split())
    if order[0] == 'add':
        ss.add(int(order[1]))
    elif order[0] == 'remove':
        ss.remove(int(order[1]))
    elif order[0] == 'find':
        if int(order[1]) in ss : print('true')
        else: print('false')
    elif order[0] == 'lower_bound':
        i = ss.bisect_left(int(order[1]))
        if i in range(len(ss)) : print(ss[i])
        else : print('None')
    elif order[0] == 'upper_bound':
        i = ss.bisect_right(int(order[1]))
        if i in range(len(ss)) : print(ss[i])
        else : print('None')
    elif order[0] == 'largest':
        if len(ss) == 0 : print('None')
        else : print(ss[-1])
    elif order[0] == 'smallest':
        if len(ss) == 0: print('None')
        else : print(ss[0])
    else: print(idx , ' error')