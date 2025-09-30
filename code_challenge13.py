# Small Diamond
for outer in range(1,3,1):
    for kalso in range(10,outer,-1):
        print(" ",end=" ") 
    for inner in range(0,outer,1):
        print("♦",end=" ") 
    for inner in range(1,outer,1):
        print("♦",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()
for outer in range(3,0,-1):
    for kalso in range(10,outer,-1):
        print(" ",end=" ") 
    for inner in range(0,outer,1):
        print("♦",end=" ")
    for inner in range(1,outer,1):
        print("♦",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()

# Big Triangle
for outer in range(1,11,1):
    for kalso in range(10,outer,-1):
        print(" ",end=" ") 
    for inner in range(0,outer,1):
        print("*",end=" ") 
    for inner in range(1,outer,1):
        print("*",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()

# Big Triangle
for outer in range(1,11,1):
    for kalso in range(10,outer,-1):
        print(" ",end=" ") 
    for inner in range(0,outer,1):
        print("*",end=" ") 
    for inner in range(1,outer,1):
        print("*",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()

# Rectangle in the middle
for outer in range(1,11,1):
    for kalso in range(6,1,-1):
        print(" ",end=" ") 
    for inner in range(0,9,1):
        print("+",end=" ") 
    print()