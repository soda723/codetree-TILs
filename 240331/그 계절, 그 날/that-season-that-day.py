def check_year(y):
    if y % 4  == 0:
        if y%100 == 0:
            if y % 400 == 0 : return 0 # 윤년임
            else : return 1 # 윤년아님
        else : return 0
    else : return 1

def checkTrue(Y, M, D):
    y = check_year(Y)
    if M in [1,3,5,7,8,10,12] : return True 
    elif M in [4,6,9,11] and D < 31 : return True
    else:
        if y : 
            if D < 29 : return True
        else: 
            if D < 30 : return True
    return False


Y, M, D = map(int, input().split())

if checkTrue(Y, M, D) :
    if 3 <= M <= 5 : print('Spring')
    elif 6 <= M <= 8 : print('Summer')
    elif 9 <= M <= 11 : print('Fall')
    else: print('Winter')
else : print(-1)