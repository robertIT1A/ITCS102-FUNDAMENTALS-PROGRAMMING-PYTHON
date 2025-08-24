#Loyalty card discount
#If the user have a loyalty card, loyalty card discount must be applied
#30% discount for loyalty card, if no loyalty card no discount

name = input("Enter your name: ")
Loyalty_card = input("Do you have a loyalty card (Yes / No): ")
amount = eval(input("Amount of the item/s: "))

if Loyalty_card.lower() == "yes": 
    discount = amount * .3 
    new_amount = amount - discount
    print("Good day", name.title(),"\n Original Price:", amount, "\n Cash Payment Discount:", discount, "\n Grand Total:", new_amount) 
    print("Thank you for coming!")
    print("Have a nice day!")
else:
    print("Good day", name.title(), "sorry your not eligible for discount.", "\nOriginal Price:", amount)
    print("Thank you for coming!")
    print("Have a nice day!")