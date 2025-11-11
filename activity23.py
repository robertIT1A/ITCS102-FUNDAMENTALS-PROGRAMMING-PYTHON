# #fruits varible
# fruit1 = 'apple'
# fruit2 = 'bananas'
# fruit3 = 'lanzones' 
# fruit4 = 'mangosteen'


# fruits = [] # empty list
# fruits.append('apple')
# fruits.append('bananas')
# fruits.append("orange")
# fruits.append('strawberries')


# append
fruits = ["apple","bananas","orange","strawberries"]
print(fruits)
# to access the item on the list
print(fruits[3])
print(fruits[-1]) # yung nasa dulo ng list
print(fruits[1:3])

# insert
# what if i want to add an item in between bananas nad orange
# first identify the index number
fruits.insert(2,"mango")
print(fruits)

# pop to delete an item at the last of the list
fruits.pop()
print(fruits)

# remove
fruits.remove("mango")
print(fruits)

# sort alpha
fruits.sort()
print(fruits)

# reverse
fruits.reverse()
print(fruits)


for langauge in fruits:
    # print(langauge)
    print(f"I want to eat {langauge}")


# list slicing
print(fruits[-3:-1])