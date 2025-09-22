#combined two loop in one loop

for outer in range(1,11,1):
    for star in range(1,outer,1): # print triangle using (*)
        print("*", end=" ") 
    for diamond in range(outer,10,1): # print reverse triangle in the same loop
        print("♦", end=" ") 
    print() # to make new line after each row