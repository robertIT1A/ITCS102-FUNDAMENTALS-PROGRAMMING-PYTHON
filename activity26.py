#  create a dictionary

Language = {'Filipino': 'Mahal kita', 'English':'I Love You', 'French': "Je t'aime", 'Spanish': 'Te amo ', 'German': 'Ich liebe dich', 'Italian': 'Ti amo', 'Japanese': 'Aishiteru', 'Mandarin Chinese': 'Wǒ ài nǐ', 'Korean': 'Saranghae', 'Russian': 'Ya lyublyu tebya', 'Arabic': 'Ana uhibbuka', 'Portuguese':' Eu te amo'}

print("LOVE LANGUAGE")
print("\n143 in every language")
for i,j in Language.items():
    print(f"\tLanguage for 143 -- {i}")
love = input("Pick one laguage: \n").capitalize()
print({Language[love]})

# notes
# pero pag gusto mo na madami ilalagay sa value gagamit ka ng [] after ng key and :

# {Keys:[Values madami]}

