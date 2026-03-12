A = int(input())
B = int(input())
if(A <= 3):
    if(A == 3 and B >= 21):
        print('spring')
    if(A < 3 and B <= 31):
        print('winter')
    if(A == 3 and B < 21):
        print('winter')
if(A <= 6 and A > 3):
    if(A == 6 and B >= 21):
        print('summer')
    if(A < 6 and B <= 31):
        print('spring')
    if(A == 6 and B < 21):
        print('spring')
if(A <= 9 and A > 6):
    if(A == 9 and B >= 21):
        print('fall')
    if(A < 9 and B <= 31):
        print('summer')
    if(A == 9 and B < 21):
        print('summer')
if(A <= 12 and A > 9):
    if(A == 12 and B >= 21):
        print('winter')
    if(A < 12 and B <= 31):
        print('fall')
    if(A == 12 and B < 21):
        print('fall')








        
