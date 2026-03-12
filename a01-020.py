A = int(input())
B = int(input())
C = int(input())
if(A < B and B < C):
    print('increasing')
elif(A > B and B > C):
    print('decreasing')
else:
    print('neither')