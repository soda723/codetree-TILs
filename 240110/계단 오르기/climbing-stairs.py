def sol(lv):
    if lv == 2 or lv == 3 : return 1
    elif lv == 1 : return 0
    else:
        return sol(lv-2) + sol(lv-3)

n = int(input())
print(sol(n)%10007)