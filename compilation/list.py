def act23():
    # append
    fruits = ["apple","bananas","orange","strawberries"]
    print("Print all the values inside the list")
    print(fruits)
    # to access the item on the list

    print("\nPrint all list one by one")
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])
    print(fruits[3])
    print(fruits[-1]) # yung nasa dulo ng list
    print(fruits[1:3])

    # insert
    # what if i want to add an item in between bananas nad orange
    # first identify the index number
    print("\nAdd mango to the middle of the list")
    fruits.insert(2,"mango")
    print(fruits)

    # pop to delete an item at the last of the list
    print("\nUse pop to delete the last item on the list")
    fruits.pop()
    print(fruits)

    # remove
    print("\nUse remove to delete the item that you want to remove on the list")
    fruits.remove("mango")
    print(fruits)

    # sort alpha
    print("\nPrint the list alphabetical using sort")
    fruits.sort()
    print(fruits)

    # reverse
    print("\nreverse the list")
    fruits.reverse()
    print(fruits)

    print("\nPrint the list")
    for langauge in fruits:
        # print(langauge)
        print(f"I want to eat {langauge}")


    # list slicing
    print(fruits[-3:-1])

def code23():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""# append
fruits = ["apple","bananas","orange","strawberries"]
print("Print all the values inside the list")
print(fruits)
# to access the item on the list

print("\nPrint all list one by one")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[-1]) # yung nasa dulo ng list
print(fruits[1:3])

# insert
# what if i want to add an item in between bananas nad orange
# first identify the index number
print("\nAdd mango to the middle of the list")
fruits.insert(2,"mango")
print(fruits)

# pop to delete an item at the last of the list
print("\nUse pop to delete the last item on the list")
fruits.pop()
print(fruits)

# remove
print("\nUse remove to delete the item that you want to remove on the list")
fruits.remove("mango")
print(fruits)

# sort alpha
print("\nPrint the list alphabetical using sort")
fruits.sort()
print(fruits)

# reverse
print("\nreverse the list")
fruits.reverse()
print(fruits)

print("\nPrint the list")
for langauge in fruits:
    # print(langauge)
    print(f"I want to eat {langauge}")


# list slicing
print(fruits[-3:-1])""")
    print("\n------------------------------------")