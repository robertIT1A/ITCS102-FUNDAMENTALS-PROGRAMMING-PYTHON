column = eval(input("Enter a number of column: "))
for num in range(1,11,1):
    for col in range(1,column+1,1):
        print(f"{num} x {col} = {num*col}",end="\t")
    print()