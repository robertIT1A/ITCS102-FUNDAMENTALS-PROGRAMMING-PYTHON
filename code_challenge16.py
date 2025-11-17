import os
import time
# os.sytstem('cls)
print("Student Information System")
print("---------------------------")


student_list = {}

def review_fav_list():
    print("This will ends in....")
    for i,s in student_list.items():
        print(f"Nickname: {i}, Favorite Person: {s}")

def countdown():
  for i in range(5):
    print(i)
    time.sleep(1)

while True:
  print("Select the option below:\n A - Add information\n B - Search a Record\n C -  Delete a Record\n D - Review a Record")

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
    for i in student_list.keys():
      for code in student_list.keys():
        print(code)
    print("Record Found")
    os.system('cls')
    continue
  elif option == "c":
    code = input("Enter Student Id: ")
    if code == Search_cod:
        remove = student_list.pop(code)
        print(f"Student{Search_cod} is remove to the list")
        countdown()
        os.system('cls')
    else:
      print("The Student Id is not found")
  elif option == "d":
    review_fav_list()
    countdown()
    os.system('cls')
  else:
    print("Invalid")
    os.system('cls')
