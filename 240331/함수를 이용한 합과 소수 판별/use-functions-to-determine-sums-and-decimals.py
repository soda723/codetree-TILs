def checkPrime(n):
    # 1과 자기 자신으로만 나눠 떨어짐
    if n == 2 or n == 3 : return True
    else:
        for i in range(2,n//2 +1):
            if n%i == 0 : 
                return False
        return True

def checkSumOdd(n):
    sum = 0
    nextn = n
    while nextn : 
        sk = nextn % 10
        nextn = nextn // 10
        sum += sk

    if sum % 2 == 0 : return True
    else : return False
    



a, b = map(int, input().split())
count = 0
for i in range(a, b +1):
    if checkPrime(i) and checkSumOdd(i):
        count += 1
print(count)