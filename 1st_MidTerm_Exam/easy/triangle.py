for i in range(1,10,1):
    for kalso in range(10,i,-1):
        print(" ",end="")
    for tri in range(1,i*2,1): # i*2 is for multiple every i that goes to tri to 2
        print("*",end="")
    print()