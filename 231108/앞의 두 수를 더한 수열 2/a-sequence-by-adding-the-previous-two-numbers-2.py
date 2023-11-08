def sol(idx):
    if idx == 1 : 
        answers.append(0)
    elif idx == 2 : 
        answers.append(1)
    else:
        answers.append(answers[idx-1]+answers[idx-2])
        
answers = [-1]
n = int(input())
for i in range(1, n+2):
    sol(i)

print(answers[n+1])