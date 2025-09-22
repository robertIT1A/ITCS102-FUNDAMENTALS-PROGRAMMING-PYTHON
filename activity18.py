num = 10 
for outer in range(1,5,1): 
    for inner in range(outer + 1, 6):
        print(num, end=" ")
        num -= 1 
    print()



#right triangle
for outer in range(1,11,1):  #This outer loop responsible for creating 1 to 10 in row
    for inner in range(1, outer): #This inner loop responsible for print number on each row or create horizontal 
        print(inner, end=" ")
    print() #Move to the next line

#reverse triangle
for outer in range(1,11,1): 
    for inner in range(outer, 10):
        print(inner, end=" ")
    print()
   


num = 1 # starting number
for outer in range(1,5,1): #This will create 4 row
    for inner in range(1, outer + 1): # this will create horizontal
        print(num, end=" ")
        num += 1 # every time that it will print, it will add 1
    print()

