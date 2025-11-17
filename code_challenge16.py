import os
# os.sytstem('cls)
print("Student Information System")
print("---------------------------")


student_list = {}

def review_fav_list():
    for i,s in student_list.items():
        print(f"Nickname: {i}, Favorite Person: {s}")

while True:
  print("Select the option below:\n A Add information\n B - Search a Record\n C -  Delete a Record\n D - Review a Record")

  option = input("Enter your option: ").lower()
  
  if option == "a":
    Search_cod = input("Student Id: ")
    first_name = input("Enter First name: ").capitalize()
    last_name = input("Enter Last name: ").capitalize()
    course = input("Student Course: ")

    student_list = {Search_cod : [first_name, last_name, course]}
    print(student_list)
    print("DATA SAVED")

  elif option == "b":
    code = input("Enter Student Id: ")
    for i in student_list.keys():
      for code in student_list.keys():
        print("Record Found")
    continue
  elif option == "c":
    code = input("Enter Student Id: ")
    remove = student_list.pop(code)
  elif option == "d":
    review_fav_list()
  else:
    print("Invalid")
