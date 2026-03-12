A = str(input())
B = str(input())
C = str(input())
if(len(A) > 5 and len(B) > 5):
    print(A[:2] + B[len(B) - 1] + C[len(C) - 1])
else:
    print(A[:1] + C + B[len(B) - 1])

