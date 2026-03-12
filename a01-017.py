A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
if(A > D ):
    print('2')
elif(A < D):
    print('1')
elif(A == D):
    if(B < E):
        print("1")
    if(B > E):
        print('2')
    elif(B == E):
        if(C < F):
            print('1')
        if(C > F):
            print('2')
        elif(C == F):
            print('0')

