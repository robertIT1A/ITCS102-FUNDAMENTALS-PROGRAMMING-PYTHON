num = eval(input("Enter a number: "))

factorial = 1
for x in range(num, 0, -1):
    factorial *= x
    print(factorial)
print("Factorial is ", factorial)