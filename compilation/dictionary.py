def act26():
    #  create a dictionary

    Language = {'Filipino': 'Mahal kita', 'English':'I Love You', 'French': "Je t'aime", 'Spanish': 'Te amo ', 'German': 'Ich liebe dich', 'Italian': 'Ti amo', 'Japanese': 'Aishiteru', 'Mandarin Chinese': 'Wǒ ài nǐ', 'Korean': 'Saranghae', 'Russian': 'Ya lyublyu tebya', 'Arabic': 'Ana uhibbuka', 'Portuguese':' Eu te amo'}

    print("\nLOVE LANGUAGE")
    print("143 in every language")
    for i,j in Language.items():
        print(f"\tLanguage for 143 -- {i}")
    love = input("Pick one laguage: \n").capitalize()
    print({Language[love]})

    # notes
    # pero pag gusto mo na madami ilalagay sa value gagamit ka ng [] after ng key and :
    # {Keys:[Values madami]}

def code26():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""Language = {'Filipino': 'Mahal kita', 'English':'I Love You', 'French': "Je t'aime", 'Spanish': 'Te amo ', 'German': 'Ich liebe dich', 'Italian': 'Ti amo', 'Japanese': 'Aishiteru', 'Mandarin Chinese': 'Wǒ ài nǐ', 'Korean': 'Saranghae', 'Russian': 'Ya lyublyu tebya', 'Arabic': 'Ana uhibbuka', 'Portuguese':' Eu te amo'}
print("\\nLOVE LANGUAGE")
print("143 in every language")
for i,j in Language.items():
    print(f"\\tLanguage for 143 -- {i}")
love = input("Pick one laguage: \\n").capitalize()
print({Language[love]})

# notes
# pero pag gusto mo na madami ilalagay sa value gagamit ka ng [] after ng key and :
# {Keys:[Values madami]}""")
    print("\n------------------------------------")


def act27():
    # dictionary 2.0
    # List of the name of your favorite person with nickname/ secret name
    import time

    print("Name of my Favorite Person")
    fav_list = {}

    tuloy = True

    def review_fav_list():
        for i,s in fav_list.items():
            print(f"Nickname: {i}, Favorite Person: {s}")
            time.sleep(1)


    def search(hanap):
        print(f"Result shows is {fav_list[hanap]}")
        time.sleep(1)

    def make_list():
            name_fav = input("Enter the Name of your Favorite Person: ").capitalize()# it is the value
            nickname = input("Enter the Nickname of that person: ")# it is the key

            fav_list[nickname] = name_fav # para pumunta sa empty list
    make_list()

    while tuloy == True:
        ulit = input("\nWould you like to add more name for your favorite person\n Type (y) for Yes\n Type (n) for No\n Type (r) to Review your list\n Type (s) to search your favorite person using thier nickname\n Type (x) to exit the program\n----> ").lower()

        if ulit == "y":
            make_list()
        elif ulit == "n":
            print("Here is your final favorite person list with there nickname")
            review_fav_list()
            print("GOOD BYE")
            exit()
        elif ulit == "r":
            review_fav_list()
        elif ulit == "s":
            code = input("\nEnter the nickname of your favorite person you are looking for: ")
            search(code)
        elif ulit == "x":
            print("Exiting.........")
            time.sleep(2)
            exit()
        else:
            print("Invalid")
            time.sleep(1)
            continue


def code27():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""import time

print("Name of my Favorite Person")
fav_list = {}

tuloy = True

def review_fav_list():
    for i,s in fav_list.items():
        print(f"Nickname: {i}, Favorite Person: {s}")
        time.sleep(1)


def search(hanap):
    print(f"Result shows is {fav_list[hanap]}")
    time.sleep(1)

def make_list():
        name_fav = input("Enter the Name of your Favorite Person: ").capitalize()# it is the value
        nickname = input("Enter the Nickname of that person: ")# it is the key

        fav_list[nickname] = name_fav # para pumunta sa empty list
make_list()

while tuloy == True:
    ulit = input("\nWould you like to add more name for your favorite person\n Type (y) for Yes\n Type (n) for No\n Type (r) to Review your list\n Type (s) to search your favorite person using thier nickname\n Type (x) to exit the program\n----> ").lower()

    if ulit == "y":
        make_list()
    elif ulit == "n":
        print("Here is your final favorite person list with there nickname")
        review_fav_list()
        print("GOOD BYE")
        exit()
    elif ulit == "r":
        review_fav_list()
    elif ulit == "s":
        code = input("\nEnter the nickname of your favorite person you are looking for: ")
        search(code)
    elif ulit == "x":
        print("Exiting.........")
        time.sleep(2)
        exit()
    else:
        print("Invalid")
        time.sleep(1)
        continue""")
    print("\n------------------------------------")