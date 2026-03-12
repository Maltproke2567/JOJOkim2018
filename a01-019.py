A = int(input())
B = int(input())
C = int(input())
if(A == B and B == C):
    print('all the same')
if(A != B and B == C):
    print('neither')
if(A == B and B != C):
    print('neither')
if(A != B and B != C):
    print('all different')

