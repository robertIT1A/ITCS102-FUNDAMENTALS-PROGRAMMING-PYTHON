# Create a To Do List
def act21():
    todo_list = []
    

    while True:
        tanong = input("Are You Want To Create Your To Do List (y/n): ")
        if tanong.lower() == "y":
            print("To Do List")
            print("Choices")
            print("A - To Add Activity \nE - To End The List")
            type= input("Please Select the Letter of Your Response (A, E) --> ")
            if type.upper() == "A":
                todo = input("Enter Your To Do List --> ")
                todo_list.append(todo.capitalize())
                print("\nA - To Add Activity \nR - Review Your List \nE - To End The List")
                type = input("Please Select the Letter of Your Response (A, R, E) --> ")
            
                if type.upper() == "R":
                    print(todo_list)
                    print("\nA - To Add Activity \nR - Review Your List \nE - To End The List")
                    type = input("\nPlease Select the Letter of Your Response (A, R, E) --> ")

            elif type.upper() == "E":
                break

            else:
                print("Invalid")
                continue
            
        else:
            break

def code21():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""todo_list = []

while True:
    tanong = input("Are You Want To Create Your To Do List (y/n): ")
    if tanong.lower() == "y":
        print("To Do List")
        print("Choices")
        print("A - To Add Activity \nE - To End The List")
        type= input("Please Select the Letter of Your Response (A, E) --> ")
        if type.upper() == "A":
            todo = input("Enter Your To Do List --> ")
            todo_list.append(todo.capitalize())
            print("\nA - To Add Activity \nR - Review Your List \nE - To End The List")
            type = input("Please Select the Letter of Your Response (A, R, E) --> ")
        
            if type.upper() == "R":
                print(todo_list)
                print("\nA - To Add Activity \nR - Review Your List \nE - To End The List")
                type = input("\nPlease Select the Letter of Your Response (A, R, E) --> ")

        elif type.upper() == "E":
            break

        else:
            print("Invalid")
            continue
        
    else:
        break""")
    print("\n------------------------------------")

# python basic game using while loop and import random
def act22():
    import random

    num = random.randint(1,10)


    tries = 4

    while tries != 0:
        guess_num = int(input("What number u guess(1-10): "))
        tries -= 1

        if guess_num != num:
            print("Sorry! Your Guess is Wrong\n")

        elif guess_num == num:
            print("Congratulation!")
            print(f"the number is {num}")
            print(f"You're remaining tries is {tries}")  
                

    print("You are out of Tries")


def code22():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""import random

num = random.randint(1,10)


tries = 4

while tries != 0:
    guess_num = int(input("What number u guess(1-10): "))
    tries -= 1

    if guess_num != num:
        print("Sorry! Your Guess is Wrong\n")

    elif guess_num == num:
        print("Congratulation!")
        print(f"the number is {num}")
        print(f"You're remaining tries is {tries}")  
            

print("You are out of Tries")""")
    print("\n------------------------------------")