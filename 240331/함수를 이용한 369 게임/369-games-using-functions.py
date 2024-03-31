def check_369(n):
    strn = str(n)
    if '3' in strn or '6' in strn or '9' in strn:
        return True
    else : return False

def check_3x(n):
    if n % 3 == 0 : return True
    else : return False

def check_count369(a, b):
    count = 0
    for i in range(a, b+1):
        if check_369(i) or check_3x(i) :
            count += 1
    return count

a, b = map(int, input().split())
print(check_count369(a, b))