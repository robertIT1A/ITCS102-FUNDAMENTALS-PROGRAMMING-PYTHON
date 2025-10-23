# ask the user to enter an odd number
# if the user input a even number print "Invalid Number"
# stop the asking if the user input 0
# print the sum of all the input odd numbers
# list all the input odd numbers


name = input("Enter your name: ")
print("-"*40)
odd = 0
con = "" # Empty list
proceed = True

while proceed == True:
    num = eval(input("Enter a number: "))
    if num % 2 == 1:
        print("Odd Detected")
        odd += num
        con += str(num) + "," # To concatenate all the odd number that the user enter
        continue
    elif num == 0: # Stop while the user input 0
        print("Loop Terminated")
        break
    else: # If the user enter a Even number
        print("Even detected")
        print("Skipping")
        continue

print(f"Hi {name}, The sum of all the EVEN numbers is {odd}")
print(f"All odd number: {con}")


