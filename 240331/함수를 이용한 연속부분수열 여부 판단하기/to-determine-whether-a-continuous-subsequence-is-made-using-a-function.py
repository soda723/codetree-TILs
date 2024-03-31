def check_bINa(lenb, alist, blist):
    if len(alist) < lenb : return False
    else:
        start = blist[0]
        for i, v in enumerate(alist):
            if start == v :
                if alist[i:i+lenb] == blist :
                    return True

    return False

n1, n2 = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

if check_bINa(n2, alist, blist): print('Yes')
else: print('No')