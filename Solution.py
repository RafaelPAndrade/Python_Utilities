import random

random.randrange(1,10)



found = False


while found != True:
    
    
    A = random.randrange(1,10)
    B = random.randrange(1,10)
    C = random.randrange(1,10)
    D = random.randrange(1,10)
    E = random.randrange(1,10)
    F = random.randrange(1,10)
    G = random.randrange(1,10)



    if (A*B+9)/C == 9 and E*F*3+G == 9 and A+3-E == 9 and (B+D+4)/F == 9 and (C-D)*G == 9:
        print(A)
        print(B)
        print(C)
        print(D)
        print(E)
        print(F)
        print(G)
        found = True
