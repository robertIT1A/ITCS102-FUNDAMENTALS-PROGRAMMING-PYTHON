# activity 24
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("select Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiptly")
    print("4. Divide")
    choice = input("Enter choice(1/2/3/4) -->")

    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter the first number -->"))
            num2 = float(input("Enter the second number -->"))
        except ValueError:
            print("Invalid input. Please Enter Numeric Value")


    if choice == "1":
        print("Result:",add(num1, num2))
    elif choice == "2":
        print("Result:",subtract(num1, num2))
    elif choice == "3":
        print("Result:",multiply(num1, num2))
    elif choice == "4":
        print("Result:",divide(num1, num2))
    else:
        print("Invalid input")



# activity 25
# act
def act_1():
    print("Hello World")

def act_2():
    x = "Roberto Guevarra"

    print("Hello World")
    print("Pogi si", x)

def act_3():
    name = input("Enter Your Name? ")
    print("Hello", name, "Welcome to the Matrix")

def act_4():
    name = input("Enter a your full name:")

    print("Your name has", len(name), "charact_ers")

def act_5():
    something = eval(input("Input number:"))

    print("The data type of something is", type(something))

    answer = 23 + something

    print("The answer is ", answer)

def act_6():
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

def act_7():   
    x = 10
    print("The original value of x is", x)
    x += 5
    x -= 10
    x *= 3
    x /= 10
    print("The value of x is", x)

def act_8():
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

def act_9():
    username = "Junior"
    password = "Good_B0y"

    name = input("Type your username:")
    print(username == name)
    password1 = input("\nType your password:")
    print(password == password1)

def act_10():
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

def act_11():
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
def act_12():
    for i in range(1,100+1,1):
        print(i, "I Love You")
        time.sleep(1)

def act_13():
    con = []

    for i in range (1, 16):
        x = int(input("Enter Whole Number: "))
        con.append (x) #append para pumunta sa []
        print(con)
    
def act_14():
    con = []


    for tanong in range (1, 5):
        x = int(input("Enter a number: "))
        con.append (x)



    for reverse in reversed (con):
        print(reverse, end="")

def act_15():
    name = "Roberto Guevarra"
    age = 19
    course = "Bachelor of Science in Information Technology"
    school = "Dalubhasaan ng Lungsod ng Lucena"

    print(f"My name is {name} and I am {age} years old. I study at {school} with a course of {course}.")

def act_16():
    for i in range(1,11,1):
        print(i, end=" ") 

def act_17():
    for sun in range(1,11,1): #This will serve as a outer loop 
        for earth in range(1,11,1): #This will serve as a inner loop 
            # Each time the outer loop runs, the inner loop runs from 1 to 10 
            print(earth, end=" ")  # print earth, followed by end=" " to prevent new line
        print()# print new line every inner loop

def act_18():
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

def act_19():
    for outer in range(1,11,1): 
        for inner in range(1, outer,1): # print triangle using (*)
            print("*", end=" ") 
        print() # to make new line after each row


#combined two loop in one loop
def act_20():
    for outer in range(1,11,1):
        for star in range(1,outer,1): # print triangle using (*)
            print("*", end=" ") 
        for diamond in range(outer,10,1): # print reverse triangle in the same loop
            print("♦", end=" ") 
        print() # to make new line after each row

# Create a To Do List
def act_21():
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


# code challenge
def code_challenge1():
    name = input("Type your name:")

    print("\t\t\t\t\t♦ \n\n \t\t\t\t♦\t\t♦ \n\n \t\t\t♦\t\t\t\t♦ \n\n \t\t♦\t\t\tLOVE U\t\t\t♦ \n\n \t♦\t\t\t\t",name,"\t\t\t♦ \n\n \t\t♦\t\t\t \t\t\t♦ \n\n \t\t\t♦\t\t\t\t♦ \n\n \t\t\t\t♦\t\t♦ \n\n \t\t\t\t\t♦")

def code_challenge2():
    name = input("Enter your Name : ")
    age = int(input("Enter your Age : "))
    address = input("Enter your Address : ")
    amount = int(input("Enter amount to Deposit : "))

    onethou = amount//1000
    onethous = amount%1000
    fivehund = onethous//500
    fivehundr = onethous%500
    twohund = fivehundr//200
    twohundr = fivehundr%200
    onehund = twohundr//100
    onehundr = twohundr%100
    fifty = onehundr//50
    fiftys = onehundr%50
    twe = fiftys//20
    twent = fiftys%20
    ten = twent//10
    tens = twent%10
    peso = tens//1
    pesos = tens%1
    print("Here is a breakdown, using Philippine denominition:")
    print(onethou,"-- 1000")
    print(fivehund,"-- 500")
    print(twohund,"-- 200")
    print(onehund,"-- 100")
    print(fifty,"-- 50")
    print(twe,"-- 20")
    print(ten,"-- 10")
    print(peso,"-- 1")

def code_challenge3():
    username = "Junior"
    password = "Good_B0y"

    import getpass
    while True: #To repeat the username until it's correct
        name = input("Enter your username: ")
        if name == username:
            print("Username Identified\n")
            break #Exit the loop
        else:
            print("Incorrect Username")
            print("Please Try Again\n")

    password1 = input("Enter your password:")
    if password1 == password:
        print("Access Complete")
    else:
        print("Access Denied")

def code_challenge4():
    number = int(input("Enter a number: "))

    if number % 2 == 0: #If your number divided into 2 it should have 0 remainder
        print("Even Number")

    else:
        print("Odd Numbers")

def code_challenge5():
    print("Welcome to Manga Recommendation!")
    print("Answer a few question to find your next read.")

    gen = input("What genre do you like? (action, romance, horror): ")

    #action
    if gen.lower() == "action":
        time = input("How long should the manga be? (short, medium, long): ")
        if time.lower() == "short":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tBlame! by Tsutomu Nihei \n\tDeadman Wonderland by Jinsei Kataoka")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tAoharu x Kikanjuu by NAOE \n\tAll You Need Is Kill by Ryōsuke Takeuchi")
        elif time.lower() == "medium":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tFreesia by Jiro Matsumoto \n\tKongō Banchō by Nakaba Suzuki")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tThe Violence Action Written by Shin Sawada, illustrated by Renji Asai \n\tChainsaw Man by Tatsuki Fujimoto")    
        elif time.lower() == "long":
            yr = input("Which decade? (2000s, 2010s): ")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tBlack Cat by Kentarou Yabuki \n\tSamurai Deeper Kyo by Akimine Kamijyo")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tAkame ga Kill! by Takahiro (story), Tetsuya Tashiro (art) \n\tHaikyu!! by Haruichi Furudate")    



    #romance
    if gen.lower() == "romance":
        time = input("How long should the manga be? (short, medium, long): ")
        if time.lower() == "short":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tLove Roma by Minoru Toyoda \n\tHoshi no Koe (Voices of a Distant Star) by Makoto Shinkai (story), Mizu Sahara (art)")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tSabaki No Mon (The Gates of Judgement) by Tsukuba Sakura \n\tHenshin Ganbou! Story: NISIO ISIN | Art: Miyokawa Masaru")
        elif time.lower() == "medium":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tKare Kano by Masami Tsuda \n\tDengeki Daisy by Kyousuke Motomi")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tKiss Me at the Stroke of Midnight by Rin Mikimoto \n\tKakafukaka by Takumi Ishida")    
        elif time.lower() == "long":
            yr = input("Which decade? (2000s, 2010s): ")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tSalad Days by Shinobu Inokuma \n\tSalad Days by Shinobu Inokuma")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tKaguya-sama: Love Is War by Aka Akasaka \n\tA Condition Called Love (Hananoi-kun to Koi no Yamai) by Megumi Morino")    

    #horror 
    if gen.lower() == "horror":
        time = input("How long should the manga be? (short, medium, long): ")
        if time.lower() == "short":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tHaunted House by Mitsukazu Mihara \n\tMantis Woman by Senno Knife")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tDissolving Classroom by Junji Ito \n\tBongcheon-Dong Ghost by Horang")
        elif time.lower() == "medium":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tAnne Freaks by Yua Kotegawa \n\tSchool Zone by Kanako Inuki")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tCreature! by Shingo Honda \n\tHappiness by Shūzō Oshimi")    
        elif time.lower() == "long":
            yr = input("Which decade? (2000s, 2010s): ")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tDescendants of Darkness by Yoko Matsushita \n\tThe Kurosagi Corpse Delivery Service by Eiji Ōtsuka (story) and Housui Yamazaki (art)")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tTokyo Ghoul by Sui Ishida  \n\tI Am a Hero by Kengo Hanazawa")    

    else:
        print("\n\tSorry but that genre isn't available. Please try again.")

def code_challenge6():
    num = eval(input("Enter a number: "))

    factorial = 1
    for x in range(num, 0, -1):
        factorial *= x 

    print("Factorial is ", factorial)

def code_challenge7():
    oddsum = 0

    for i in range(10):
        num = int(input("Enter a number: "))
        if num % 2 != 0:
            oddsum += num

    print("The sumation of all odd numbers is", oddsum)

def code_challenge8():
    print("MULTIPLACATION TABLE MAKER")
    num = eval(input("Enter a number: "))

    print(num)
    for i in range (1, 10+1):
        mul = num * i
        
        print(num, "x", i, "=", mul)

def code_challenge9():
    print("COUNTDOWN TIMER SIMULATOR")
    time = int(input("Enter the starting number for countdown:"))

    print("Countdown started:")
    for i in range (time, 0, -1):
        print(i)
    print("Liftoff!")

def code_challenge10():
    for outer in range(1,11,1):
        for kalso in range(10,outer,-1): # it will print reverse triangle 
            print(" ",end=" ") # but because of " " is will provide space/blank
        for inner in range(0,outer,1):
            print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()


def code_challenge11():
    # make a diamond using for loop

    #create triangle
    for outer in range(1,11,1):
        for kalso in range(10,outer,-1): # it will print reverse triangle 
            print(" ",end=" ") # but because of " " is will provide space/blank
        for inner in range(0,outer,1):
            print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    #reverse triangle
    for outer in range(9,0,-1):
        for kalso in range(10,outer,-1): # it will print reverse triangle 
            print(" ",end=" ") # but because of " " is will provide space/blank
        for inner in range(0,outer,1):
            print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

def code_challenge12():
    for i in range(1,7,1):
        for kalso in range(7,i,-1):
            print(" ",end=" ")
        for s in range(i,0,-1):
            print(s,end=" ")
        for s in range(2,kalso,1):
            print(s,end=" ")
        print()

def code_challenge13():
    for outer in range(1,3,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("♦",end=" ") 
        for inner in range(1,outer,1):
            print("♦",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()
    for outer in range(3,0,-1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("♦",end=" ")
        for inner in range(1,outer,1):
            print("♦",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Big Triangle
    for outer in range(1,7,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("*",end=" ") 
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Big Triangle
    for outer in range(1,13,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("*",end=" ") 
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Big Triangle
    for outer in range(1,15,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("*",end=" ") 
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Rectangle in the middle
    for outer in range(1,11,1):
        for kalso in range(11,1,-1):
            print(" ",end=" ") 
        for inner in range(0,9,1):
            print("+",end=" ") 
        print()


def code_challenge14():
    name = input("Enter your name: ")
    print("-"*40)
    odd = 0
    con = "" # Empty list
    proceed = True

    while proceed == True:
        num = eval(input("Enter a number: "))
        if num % 2 == 1: # to Identify if the number is Odd number
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


def code_challenge15():
    # Anime list
    # Using list operations
    print("Anime Title List")

    anime_list = [] # empty list
    proceed = True   

    while proceed == True:
        anime = input("Enter the title of an Anime (or type 'end' to end): ")
        if anime == "end": # stopper
            print("All done,You are now exiting!! ")
            break    # terminate the loop

        else: # proceed
            print(f"'{anime}' added to the your Anime List") # every time that you answer, it will show up unless the user type "end"
            anime_list.append(anime) # all title that the user enter will be go to empty list

    print(f"Here All the Title of your Anime:") # after user type "end" it will show up
    for i in anime_list:     # print all the anime that the user enter
        print(f"- {i}")

    
def code_challenge16():
    import os
    import time
    import json
    # os.sytstem('cls)
    print("Student Information System")
    print("---------------------------")


    student_list = {}

    def review_fav_list():
        for i,s in student_list.items():
            print(f"Student Id: {i}, Student Name: {s}")
        print("This will ends in....")

    def delete():
        print(f"Student Id number {student_list[code]} is remove to the list")
        countdown()
        os.system('cls')
        # code = input("Enter Student ID to delete: ")
        # if code in student_list:
        #   removed_student = student_list.pop(code)  # Safely remove by key
        #   print(f"Student ID {code} ({removed_student[0]} {removed_student[1]}{removed_student[2]}) has been removed from the list.")
        #   countdown()
        #   os.system('cls')

  

    def countdown():
        for i in range(1,4):
            print(i)
            time.sleep(1)

    while True:
        os.system("cls")
        print("Select the option below:\n A - Add information\n B - Search a Record\n C - Delete a Record\n D - Review a Record\n E - Modify the List\n F - Export Student Record\n G - Import Student Record\n H - Exit the program")

        option = input("Enter your option: ").lower()
        
        if option == "a":
            Search_cod = input("Student Id: ")
            first_name = input("Enter First name: ").capitalize()
            last_name = input("Enter Last name: ").capitalize()
            course = input("Student Course: ").upper()

            # student_list = {Search_cod : [first_name, last_name, course]}
            student_list[Search_cod] = [first_name, last_name, course]
            print("DATA SAVED")
            countdown()
            os.system('cls')

        elif option == "b":
            code = input("Enter Student Id: ")
            print(f"Result shows is {student_list[code]}")
            print("Record Found")
            countdown()
            os.system('cls')
            continue
        elif option == "c":
            code = input("Enter Student Id: ")
            if code in student_list: # dito nagsearch na ako pano mawala yung pinaka unang keys kasi yung last lagi yung pede lang madelete
                del student_list[code]
                print(f"Student Id number {student_list[code]} is remove to the list")
                countdown()
                os.system('cls')
            else:
                print("The Student Id is not found")
        elif option == "d":
            review_fav_list()
            countdown()
            os.system('cls')
        elif option == "e":
            while True:
                code = input("Enter the code you want to change: ")
                print(f"Result shows is {student_list[code]}")
                edit = int(input("Option to edit\n Type the number\n 1. First name\n 2. Last name\n 3. Course\n----> "))
                if edit == 1:
                    print("Editing First Name")
                    new = input("Enter a new First Name: ").capitalize()
                    student_list[code][0] = new # para mabago yung values
                elif edit == 2:
                    print("Editing Last Name")
                    new = input("Enter a new Last Name: ").capitalize()
                    student_list[code][1] = new
                elif edit == 3:
                    print("Editing Course")
                    new = input("Enter a new Course: ").upper()
                    student_list[code][2] = new
                else:
                    print("Invalid choose")
                print(f"{student_list[code]} Is the new Student Data")
                option = input("Do you want to edit again?(yes/no) ").lower()
                if option == "yes":
                    continue
                elif option == "no":
                    os.system("cls")
                break
            # isa = input("Do you want to edit another data")
            # if option == "yes":
            #   continue
            # elif option == "no":
            #   os.system("cls")
            #   break
            
        elif option == "f":
            os.system("cls")
            print("Export Student Record")
                    # file name, read(r) for Import/ write(w) for Export
            with open('student_record.json','w') as new_file:
                json.dump(student_list, new_file, indent=4)

            print("DATA EXPORTED TO JSON")
            countdown()
            os.system('cls')

        elif option == "g":
            os.system("cls")
            print("Import Student Record")
                    # file name, read(r) for Import/ write(w) for Export
            with open('student_record.json','r') as new_file:
                student_json = json.load(new_file)

            student_list = student_json
            print("DATA IMPORTED TO JSON")
            countdown()
            os.system('cls')

        elif option == "h":
            os.system("cls")
            print("Exiting The Program........")
            countdown()
            os.system("cls")
            exit()

        else:
            print("Invalid")
            os.system('cls')