#ODD number summation
#Enter 10 numbers
#add all odd numbers


oddsum = 0

for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        oddsum += num

print("The sumation of all odd numbers is", oddsum)