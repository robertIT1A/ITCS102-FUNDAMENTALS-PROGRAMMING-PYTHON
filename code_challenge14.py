# ask the user to enter an even number
# if the user input a odd number print "Invalid Number"
# stop the asking if the user input 0
# print the sum of all the input even numbers
# list all the input even numbers


name = input("Enter your name: ")
print("-"*40)
num = 1
add = 0
con = "\r"

while num != 0:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even Number")
        add += num 
        con += str(num) + ","

    else:
        print("Invalid number") 

print("Loop Terminated")
print(f"Hi {name}, The sum of all the EVEN numbers is {add}")
print(f"All the EVEN numbers you input is {con}")
