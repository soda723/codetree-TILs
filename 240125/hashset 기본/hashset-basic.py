n = int(input())
hashset = set()
for _ in range(n):
    order, num = input().split()
    num = int(num)
    if order == 'add':
        hashset.add(num)
    elif order == 'remove':
        hashset.remove(num)
    elif order == 'find':
        if num in hashset : print('true')
        else : print('false')
    else : print('error')