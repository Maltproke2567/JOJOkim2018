numbers = list(map(int, input().split()))
S = ""
for i in range(0, 10):
    A = True
    for j in range(0, i):
        if(numbers[j] == numbers[i]):
            A = False
            break
        if(numbers[j] != numbers[i]):
            A = True
            continue
    if(A == True):
        S = S + str(numbers[i]) + " "
print(S)


    
    
    


    