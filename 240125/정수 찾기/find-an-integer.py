n = int(input())
arr_a = set(map(int, input().split()))
m = int(input())
arr_b = list(map(int, input().split()))

for b in arr_b :
    if b in arr_a : print(1)
    else : print(0)