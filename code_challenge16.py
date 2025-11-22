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
