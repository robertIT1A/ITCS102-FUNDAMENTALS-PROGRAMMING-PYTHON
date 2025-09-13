#reverse loop
#contatenate all the number in reverse

con = []


for tanong in range (1, 16):
    x = int(input("Enter a number: "))
    con.append (x)



for reverse in reversed (con):

    print(reverse, end="") #end para mag leave ng space
