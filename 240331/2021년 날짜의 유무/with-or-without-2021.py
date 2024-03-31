def checkDay(M, D):
    day30s = [4,6,9,11]
    day31s = [1,3,5,7,8,10,12]

    if M in day30s and 1 <= D <= 30 : return True
    elif M in day31s and 1 <= D <= 31 : return True
    elif M == 2 and 1<= D <= 28 : return True
    return False


M, D = map(int, input().split())
if checkDay(M, D) : print('Yes')
else : print('No')