#Ask the user to input a number
#Using loop to print the multiplication table for that number

print("MULTIPLACATION TABLE MAKER")
num = eval(input("Enter a number: "))

for i in range (1, 11):
    mul = num * i
    print(num, "x", i, "=", mul)