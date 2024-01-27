a, op , b = input().split()

if op == '+' :
    print(a,'+',b,'=',int(a)+int(b))
elif op == '-':
    print(a,'-',b,'=',int(a)-int(b))
elif op == '*':
     print(a,'*',b,'=',int(a)*int(b))
else :
     print(a,'/',b,'=',int(a)//int(b))