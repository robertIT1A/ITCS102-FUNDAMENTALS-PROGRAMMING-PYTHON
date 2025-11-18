import os
import time
# os.sytstem('cls)
print("Student Information System")
print("---------------------------")


student_list = {}

def review_fav_list():
    for i,s in student_list.items():
        print(f"Student Id: {i}, Student Name: {s}")
    print("This will ends in....")

def delete():
  # code = input("Enter Student ID to delete: ")
  # if code in student_list:
  #   removed_student = student_list.pop(code)  # Safely remove by key
  #   print(f"Student ID {code} ({removed_student[0]} {removed_student[1]}{removed_student[2]}) has been removed from the list.")
  #   countdown()
  #   os.system('cls')

  remove = student_list.remove(code)
  print(f"Student Id number {Search_cod} is remove to the list")
  countdown()
  os.system('cls')

def countdown():
  for i in range(5):
    print(i)
    time.sleep(1)

while True:
  print("Select the option below:\n A - Add information\n B - Search a Record\n C -  Delete a Record\n D - Review a Record\n E - Modify the List")

  option = input("Enter your option: ").lower()
  
  if option == "a":
    Search_cod = input("Student Id: ")
    first_name = input("Enter First name: ").capitalize()
    last_name = input("Enter Last name: ").capitalize()
    course = input("Student Course: ")

    # student_list = {Search_cod : [first_name, last_name, course]}
    student_list[Search_cod] = [first_name, last_name, course]
    print("DATA SAVED")
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
        # delete()
    else:
      print("The Student Id is not found")
  elif option == "d":
    review_fav_list()
    countdown()
    os.system('cls')
  elif option == "e":
     pass
  else:
    print("Invalid")
    os.system('cls')
