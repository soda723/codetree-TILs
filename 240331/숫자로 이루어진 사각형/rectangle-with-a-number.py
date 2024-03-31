def drawgrid(n):
    order = '123456789'
            #012345678
    count = 0
    for _ in range(n):
        for _ in range(n):
            print(order[count], end = ' ')
            if count == 8 : count = 0
            else : count += 1
        print()
n = int(input())
drawgrid(n)