for i in range(1,7,1):
    for kalso in range(7,i,-1):
        print(" ",end=" ")
    for s in range(i,0,-1):
        print(s,end=" ")
    for s in range(2,kalso,1):
        print(s,end=" ")
    print()