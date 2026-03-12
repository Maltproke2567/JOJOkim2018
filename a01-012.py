A = int(input())
B = str(input())
C = A%10
D = A//10
C = C * 10 + D
E = A * C
F = A - C 
if(B == '+'):
    print(A, '-', C, '=', E)
if(B == '*'):
    print(A, '/', C, '=', F)
    


