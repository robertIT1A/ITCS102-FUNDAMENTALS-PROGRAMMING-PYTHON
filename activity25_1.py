def act1():
    print("Hello World")

def act2():
    x = "Roberto Guevarra"

    print("Hello World")
    print("Pogi si", x)

def act3():
    name = input("Enter Your Name? ")
    print("Hello", name, "Welcome to the Matrix")

def act4():
    name = input("Enter a your full name:")

    print("Your name has", len(name), "characters")

def act5():
    something = eval(input("Input number:"))

    print("The data type of something is", type(something))

    answer = 23 + something

    print("The answer is ", answer)

def act6():
    x = eval(input("Enter the value of x : "))
    y = eval(input("Enter the value of y : "))
    s = x + y
    d = x - y
    p = x * y
    q = x / y
    print("\nThe sum of", x, "and", y, "is" ,s)
    print("The difference of", x, "and", y, "is", d) 
    print("The product of", x, "and",y, "is",p) 
    print("The quotient of",x, "and",y, "is",q)
    print(x, "exponent by", y, "is",x**y)
    print ("The remainder of", x, "and",y, "is", x % y) 
    print ("The floor division of",x, "and", y, "is", x//y)

def act7():   
    x = 10
    print("The original value of x is", x)
    x += 5
    x -= 10
    x *= 3
    x /= 10
    print("The value of x is", x)

def act8():
    balance = 1000
    amount = 0

    amount = int(input("Enter the amount to withdraw:"))
    print(balance >= amount)
    if balance >= amount:
        print("Here's you", amount, "Thank you!")
        ramaining = balance - amount
        print("Your remaining balance is", ramaining)
    elif balance <= amount:
        print("You have not enough balance, please try again!")
        print("Your balance is only", balance)

def act9():
    username = "Junior"
    password = "Good_B0y"

    name = input("Type your username:")
    print(username == name)
    password1 = input("\nType your password:")
    print(password == password1)

def act10():
    name = input("Enter your name: ")
    Loyalty_card = input("Do you have a loyalty card (Yes / No): ")
    amount = eval(input("Amount of the item/s: "))

    if Loyalty_card.lower() == "yes": 
        discount = amount * .3 
        new_amount = amount - discount
        print("Good day", name.title(),"\n Original Price:", amount, "\n Cash Payment Discount:", discount, "\n Grand Total:", new_amount) 
        print("Thank you for coming!")
        print("Have a nice day!")
    else:
        print("Good day", name.title(), "sorry your not eligible for discount.", "\nOriginal Price:", amount)
        print("Thank you for coming!")
        print("Have a nice day!")

def act11():
    num = int(input("Enter a number: "))

    if num >= 1 and num % 2 == 0:
        print("Possitive and Even")

    elif num >= 1 and num % 2 != 0:
        print("Possitive and Odd")

    elif num <= -1 and num % 2 == 0:
        print("Negative and Even")

    elif num % 2 != 0 and num <= -1:
        print("Negative and Odd")

    else:
        print("Zero")

import time
def act12():
    for i in range(1,100+1,1):
        print(i, "I Love You")
        time.sleep(1)

def act13():
    con = []

    for i in range (1, 16):
        x = int(input("Enter Whole Number: "))
        con.append (x) #append para pumunta sa []
        print(con)
    
def act14():
    con = []


    for tanong in range (1, 5):
        x = int(input("Enter a number: "))
        con.append (x)



    for reverse in reversed (con):
        print(reverse, end="")

def act15():
    name = "Roberto Guevarra"
    age = 19
    course = "Bachelor of Science in Information Technology"
    school = "Dalubhasaan ng Lungsod ng Lucena"

    print(f"My name is {name} and I am {age} years old. I study at {school} with a course of {course}.")

def act16():
    for i in range(1,11,1):
        print(i, end=" ") 

def act17():
    for sun in range(1,11,1): #This will serve as a outer loop 
        for earth in range(1,11,1): #This will serve as a inner loop 
            # Each time the outer loop runs, the inner loop runs from 1 to 10 
            print(earth, end=" ")  # print earth, followed by end=" " to prevent new line
        print()# print new line every inner loop

def act18():
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

def act19():
    for outer in range(1,11,1): 
        for inner in range(1, outer,1): # print triangle using (*)
            print("*", end=" ") 
        print() # to make new line after each row


#combined two loop in one loop
def act20():
    for outer in range(1,11,1):
        for star in range(1,outer,1): # print triangle using (*)
            print("*", end=" ") 
        for diamond in range(outer,10,1): # print reverse triangle in the same loop
            print("♦", end=" ") 
        print() # to make new line after each row

# Create a To Do List
def act21():
    todo_list = []
    tanong = input("Are You Want To Create Your To Do List (y/n): ")


    if tanong.lower() == "y":
        print("To Do List")
        print("Choices")
        print("A - To Add Activity \nE - To End The List")
        type= input("Please Select the Letter of Your Response (A, E) --> ")
        while type.upper() == "A":
            todo = input("Enter Your To Do List --> ")
            todo_list.append(todo.capitalize())
            print("\nA - To Add Activity \nR - Review Your List \nE - To End The List")
            type = input("Please Select the Letter of Your Response (A, R, E) --> ")
        
            while type.upper() == "R":
                print(todo_list)
                print("\nA - To Add Activity \nR - Review Your List \nE - To End The List")
                type = input("\nPlease Select the Letter of Your Response (A, R, E) --> ")

        while type.upper() == "E":
            exit()
        
    else:
        exit()
