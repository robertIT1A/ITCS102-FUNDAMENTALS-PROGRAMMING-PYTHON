#Identify the whole number
#Odd or Even
#Possitive or Negative

num = int(input("Enter a number: "))

if num >= 1 and num % 2 == 0:
    print("Possitive and Even")

elif num >= 1 and num % 2 != 0:
    print("Possitive and Odd")

elif num <= -1 and num % 2 == 0:
    print("Negative and Even")

elif num %2 != 0 and num <= -1:
    print("Negative and Odd")

else:
    print("Zero")