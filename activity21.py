# while loop

# isClean = True

# while isClean == True:
#     ask = input("are you clean already (y/n) --> ")

#     if ask.lower() == "y":
#         print("loop continue")
#         continue

#     else:
#         print("loop stops")
#         break



# Create a To Do List
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
