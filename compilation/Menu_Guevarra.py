from Variables_and_Printing_Output import *
from datatypes import *
from Operation import *
from Condition_Statement import *
from list import *
from for_loop import *
from while_loop import *
from definition import *
from dictionary import *
from game import *
import time
import os

def countdown():
    print("This program ends in............")
    for i in range(1,4):
        print(i,"..............................")
        time.sleep(1)

def proceed():
    tuloy =  input("\nPress Enter if you are finish in this program ")

    if tuloy == "":
        countdown()
    else:
        print("You typed something, but the program will still continue.")
        countdown()

def Variables_printing():
    while True:
        os.system("cls")
        print("_____________________________________________") 
        print("|         Variables and Printing Menu        |") 
        print("|                                            |") 
        print("|             1.Activity 1                   |") 
        print("|             2.Activity 2                   |") 
        print("|             3.Activity 3                   |") 
        print("|             4.Activity 15                  |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code1()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act1()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code2()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act2()
                    proceed()
                else:
                    pass
                
            elif activity_number == 3:
                code3()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act3()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 4:
                code15()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act15()
                    proceed()
                else:
                    pass
                    countdown()
        else:
                print("The activity number is not avalable")
                countdown()

def Data_types():
    while True:
        os.system("cls")
        print("_____________________________________________") 
        print("|               Data Types Menu              |") 
        print("|                                            |") 
        print("|             1.Activity 4                   |") 
        print("|             2.Activity 5                   |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code4()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act4()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code5()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act5()
                    proceed()
                else:
                    pass
                    countdown()
        else:
                print("The activity number is not avalable")
                countdown()

def operation():
    while True:
        os.system("cls")
        print("_____________________________________________") 
        print("|                Operation Menu              |") 
        print("|                                            |") 
        print("|             1.Assignment Operation         |") 
        print("|             2.Logical Operation            |") 
        print("|             3.Operator Precendence         |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code7()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act7()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code9()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act9()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 3:
                code6()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act6()
                    proceed()
                else:
                    pass
                    countdown()
        else:
                print("The activity number is not avalable")
                countdown()

def Condition():
    while True:
        os.system("cls")
        print("_____________________________________________") 
        print("|          Condition Statement Menu          |") 
        print("|                                            |") 
        print("|             1.Activity 8                   |") 
        print("|             2.Activity 10                  |") 
        print("|             3.Activity 11                  |")  
        print("|             0.Back to Main Menu            |") 
        print("|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code8()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act8()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code10()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act10()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 3:
                code11()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act11()
                    proceed()
                else:
                    pass
                    countdown()
        else:
                print("The activity number is not avalable")
                countdown()

def forloop():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|              For Loop Menu             |") 
        print("|                                        |") 
        print("|             1.Activity 12              |")
        print("|             2.Activity 13              |")
        print("|             3.Activity 14              |")
        print("|             4.Activity 16              |")
        print("|             5.Activity 17              |")
        print("|             6.Activity 18              |")  
        print("|             7.Activity 19              |")
        print("|             8.Activity 20              |")
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code12()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act12()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code13()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act13()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 3:
                code14()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act14()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 4:
                code16()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act16()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 5:
                code17()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act17()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 6:
                code18()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act18()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 7:
                code19()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act19()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 8:
                code20()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act20()
                    proceed()
                else:
                    pass
                    countdown()
        else:
                print("The activity number is not avalable")
                countdown()

def WhileLoop():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|             While Loop Menu            |") 
        print("|                                        |") 
        print("|             1.Activity 21              |")
        print("|             2.Activity 22              |")
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            # display_zero()
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code21()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act21()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code22()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act22()
                    proceed()
                else:
                    pass
                    countdown() 
        else:
                print("The activity number is not avalable")
                countdown()   

def looping():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|             Looping Section            |") 
        print("|                                        |") 
        print("|             1.For Loop                 |")  
        print("|             2.While Loop               |") 
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                forloop()
            elif activity_number == 2:
                WhileLoop()
        else:
                print("The activity number is not avalable")
                countdown()

def List():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|               List Menu                |") 
        print("|                                        |") 
        print("|             1.Activity 23              |")  
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code23()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act23()
                    proceed()
                else:
                    pass
                    countdown()
        else:
                print("The activity number is not avalable")
                countdown()

def definition():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|             Definition Menu            |") 
        print("|                                        |") 
        print("|             1.Activity 24              |")  
        print("|             2.Activity 25              |")  
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code24()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act24()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code25()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act25()
                    proceed()
                else:
                    pass
                    countdown()
            else:
                print("The activity number is not avalable")
                countdown()

def dictionary():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|             Dictionary Menu            |")  
        print("|                                        |") 
        print("|             1.Activity 26              |")  
        print("|             2.Activity 27              |")  
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code26()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act26()
                    proceed()
                else:
                    pass
                    countdown()
            elif activity_number == 2:
                code27()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act27()
                    proceed()
                else:
                    pass
                    countdown()
            else:
                print("The activity number is not avalable")
                countdown()

def pygame():
    while True:
        os.system("cls")
        print("__________________________________________") 
        print("|             Dictionary Menu            |")  
        print("|                                        |") 
        print("|             1.Activity 28              |")   
        print("|             0.Back to Main Menu        |") 
        print("|________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 9:
            if activity_number == 1:
                code28()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act28()
                    proceed()
                else:
                    pass
                    countdown()
            else:
                print("The activity number is not avalable")
                countdown()  

def code_challenge():
    while True:
        os.system("cls")
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("___________________________________________________________________________________") 
        print("|                              Code Challenge Menu                                |") 
        print("|_________________________________________________________________________________|") 
        print("|           1.Code Challenge 1           |           9.Code Challenge 9           |")  
        print("|           2.Code Challenge 2           |           10.Code Challenge 10         |")
        print("|           3.Code Challenge 3           |           11.Code Challenge 11         |")
        print("|           4.Code Challenge 4           |           12.Code Challenge 12         |")
        print("|           5.Code Challenge 5           |           13.Code Challenge 13         |")
        print("|           6.Code Challenge 6           |           14.Code Challenge 14         |")
        print("|           7.Code Challenge 7           |           15.Code Challenge 15         |")
        print("|           8.Code Challenge 8           |           16.Code Challenge 16         |")  
        print("|                                        |           0.Back to Main Menu          |") 
        print("|_________________________________________________________________________________|") 
        activity_number = int(input("Enter the Code Challenge number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            break
        elif 1 <= activity_number <= 100:
            if activity_number == 1:
                code_challenge1()
                countdown()
            elif activity_number == 2:
                code_challenge2()
                countdown()
            elif activity_number == 3:
                code_challenge3()
                countdown()
            elif activity_number == 4:
                code_challenge4()
                countdown()
            elif activity_number == 5:
                code_challenge5()
                countdown()
            elif activity_number == 6:
                code_challenge6()
                countdown()
            elif activity_number == 7:
                code_challenge7()
                countdown()
            elif activity_number == 8:
                code_challenge8()
                countdown()
            elif activity_number == 9:
                code_challenge9()
                countdown()
            elif activity_number == 10:
                code_challenge10()
                countdown()
            elif activity_number == 11:
                code_challenge11()
                countdown()
            elif activity_number == 12:
                code_challenge12()
                countdown()
            elif activity_number == 13:
                code_challenge13()
                countdown()
            elif activity_number == 14:
                code_challenge14()
                countdown()
            elif activity_number == 15:
                code_challenge15()
                countdown()
            elif activity_number == 16:
                code_challenge16()
                countdown()
        else:
            print("The code challenge number is not avalable")
            countdown()


def display_close():
    os.system("cls") 
    open = [ 
        # "\n\n",
        "Main Menu appears in 3 seconds", 
        "3..................................................", 
        "2..................................................", 
        "1..................................................", 
        "                                                   ", 
    ] 
    delay = 30
    timer_exit(open, delay) 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def  timer_exit(open, delay): 
    try: 
        for line in open: 
            print("\r", end="") 
            for c in line: 
                print(c, end="", flush=True) 
                time.sleep(delay / 1000.0) 
            time.sleep(delay * 15 / 1000.0) 
    except KeyboardInterrupt: 
        pass 

def seach_menu():
    while True:
        print(" ______________________________________________")         
        print("|                 Choose here                  |") 
        print("|______________________________________________|") 
        print("|                Search Menu:                  |") 
        print("|                                              |") 
        print("|            1.Activity                        |") 
        print("|            2.Code Challenge                  |") 
        print("|            0.Exit                            |") 
        print("|______________________________________________|") 

        option = int(input("Type the number that you want to search: "))

        if option == 0:
            break
        elif option == 1:
            activity = int(input("Enter the activity number that you want to access: "))
            if activity == 1:
                code1()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act1()
                    proceed()
            elif activity == 2:
                code2()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act2()
                    proceed()
            elif activity == 3:
                code3()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act3()
                    proceed()
            elif activity == 4:
                code4()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act4()
                    proceed()
            elif activity == 5:
                code5()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act5()
                    proceed()
            elif activity == 6:
                code6()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act6()
                    proceed()
            elif activity == 7:
                code7()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act7()
                    proceed()
            elif activity == 8:
                code8()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act8()
                    proceed()
            elif activity == 9:
                code9()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act9()
                    proceed()
            elif activity ==10:
                code10()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act10()
                    proceed()
            elif activity == 11:
                code11()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act1()
                    proceed()
            elif activity == 12:
                code12()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act12()
                    proceed()
            elif activity == 13:
                code13()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act13()
                    proceed()
            elif activity == 14:
                code14()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act14()
                    proceed()
            elif activity == 15:
                code15()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act15()
                    proceed()
            elif activity == 16:
                code16()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act16()
                    proceed()
            elif activity == 17:
                code17()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act17()
                    proceed()
            elif activity == 18:
                code18()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act18()
                    proceed()
            elif activity == 19:
                code19()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act19()
                    proceed()
            elif activity == 20:
                code20()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act20()
                    proceed()
            elif activity == 21:
                code21()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act21()
                    proceed()
            elif activity == 22:
                code22()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act22()
                    proceed()
            elif activity == 23:
                code23()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act23()
                    proceed()
            elif activity == 24:
                code24()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act24()
                    proceed()
            elif activity == 25:
                code25()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act25()
                    proceed()
            elif activity == 26:
                code26()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act26()
                    proceed()
            elif activity == 27:
                code27()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act27()
                    proceed()
            elif activity == 28:
                code28()
                time.sleep(1)
                ask = input("\nDo you want to access this program? (Yes/No) ---> ").lower()
                if ask == "yes":
                    print("Output:\n")
                    act28()
                    proceed()
            else:
                print("Sorry!, that activity number is not available.")
        elif option == 2:
            activity_number = int(input("Enter the Code challenge number that you want to access: "))
            if activity_number == 1:
                code_challenge1()
                countdown()
            elif activity_number == 2:
                code_challenge2()
                countdown()
            elif activity_number == 3:
                code_challenge3()
                countdown()
            elif activity_number == 4:
                code_challenge4()
                countdown()
            elif activity_number == 5:
                code_challenge5()
                countdown()
            elif activity_number == 6:
                code_challenge6()
                countdown()
            elif activity_number == 7:
                code_challenge7()
                countdown()
            elif activity_number == 8:
                code_challenge8()
                countdown()
            elif activity_number == 9:
                code_challenge9()
                countdown()
            elif activity_number == 10:
                code_challenge1()
                countdown()
            elif activity_number == 11:
                code_challenge11()
                countdown()
            elif activity_number == 12:
                code_challenge12()
                countdown()
            elif activity_number == 13:
                code_challenge13()
                countdown()
            elif activity_number == 14:
                code_challenge14()
                countdown()
            elif activity_number == 15:
                code_challenge15()
                countdown()
            elif activity_number == 16:
                code_challenge16()
                countdown()

def main():
    os.system("cls")
    name = input("Enter your name: ").title() 
    os.system("cls")
    open = [ 
        f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         Giving Access to {name}", 
        f"         Hello, {name}           ", 
        "         Welcome to Finals Compilation         ",
        "         Generated by Roberto B. Guevarra Jr.                           ", 
        "         Please wait a few seconds                            ", 
        "                                                        ", 
    ] 
    delay = 40 
    timer_exit(open, delay) 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    display_close()
    while True:
        os.system("cls")
        print(" ______________________________________________")         
        print("|                 Choose here                  |") 
        print("|______________________________________________|") 
        print("|                  Main Menu:                  |") 
        print("|                                              |") 
        print("|            1.Variables and Printing          |") 
        print("|            2.Data Types                      |") 
        print("|            3.Operation                       |") 
        print("|            4.Condition Statement             |")
        print("|            5.Looping                         |") 
        print("|            6.List                            |") 
        print("|            7.Definition                      |") 
        print("|            8.Dictionary                      |")
        print("|            9.Pygame                          |")
        print("|            10.Code Challenge                 |")
        print("|            11.Search Menu                    |")
        print("|            0.Exit                            |") 
        print("|______________________________________________|") 
        choice = int(input("Enter your choice: "))
        if choice == 0:
            os.system("cls")
            print(f"GoodBye {name}!\nThank you for visiting this proggram")
            time.sleep(1)
            print("\nThis program is brought to you by \n\tRoberto B. Guevarra Jr.\n\tBSIT-1A\n\tGithub_username: robertIT1A")
            countdown()
            exit()
        elif choice == 1:
            Variables_printing()
        elif choice == 2:
            Data_types()
        elif choice == 3:
            operation()
        elif choice == 4:
            Condition()
        elif choice == 5:
            looping()
        elif choice == 6:
            List()
        elif choice == 7:
            definition()
        elif choice == 8:
            dictionary()  
        elif choice == 9:
            pygame()   
        elif choice == 10:
            code_challenge()
        elif choice == 11:
            seach_menu()
        else:
            print("Invalid")
            continue
main()