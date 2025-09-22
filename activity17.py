# using loop print 1 to 10 horizontal 
# print 1 to 10 per each row

for sun in range(1,11,1): #This will serve as a outer loop 
    for earth in range(1,11,1): #This will serve as a inner loop 
        # Each time the outer loop runs, the inner loop runs from 1 to 10 
        print(earth,)  # print earth, followed by end=" " to prevent new line
    print()# print new line every inner loop
    
