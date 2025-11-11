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
            

print("\r\rYou are out of Tries")
