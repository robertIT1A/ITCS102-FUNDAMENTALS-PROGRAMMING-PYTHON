# make a diamond using for loop

#create triangle
for outer in range(1,11,1):
    for kalso in range(10,outer,-1): # it will print reverse triangle 
        print(" ",end=" ") # but because of " " is will provide space/blank
    for inner in range(0,outer,1):
        print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
    for inner in range(1,outer,1):
        print("*",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()

#reverse triangle
for outer in range(9,0,-1):
    for kalso in range(10,outer,-1): # it will print reverse triangle 
        print(" ",end=" ") # but because of " " is will provide space/blank
    for inner in range(0,outer,1):
        print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
    for inner in range(1,outer,1):
        print("*",end=" ")
    for kalso in range(10,outer,-1):
        print(" ",end=" ")
    print()