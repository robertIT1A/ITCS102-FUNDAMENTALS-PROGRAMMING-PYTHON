#ODD number summation
#Enter 10 numbers
#add all odd numbers

oddsum = []
evensum = []
for i in range(5):
    num = eval(input("Enter a number: "))
    if num // 3 == 0:
        oddsum.append (num)
        print(num, "odd")
    else:
        evensum.append (num)
        print(num, "even")

print(oddsum)