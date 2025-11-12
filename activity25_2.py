def code1():
    name = input("Type your name:")

    print("\t\t\t\t\t♦ \n\n \t\t\t\t♦\t\t♦ \n\n \t\t\t♦\t\t\t\t♦ \n\n \t\t♦\t\t\tLOVE U\t\t\t♦ \n\n \t♦\t\t\t\t",name,"\t\t\t♦ \n\n \t\t♦\t\t\t \t\t\t♦ \n\n \t\t\t♦\t\t\t\t♦ \n\n \t\t\t\t♦\t\t♦ \n\n \t\t\t\t\t♦")

def code2():
    name = input("Enter your Name : ")
    age = int(input("Enter your Age : "))
    address = input("Enter your Address : ")
    amount = int(input("Enter amount to Deposit : "))

    onethou = amount//1000
    onethous = amount%1000
    fivehund = onethous//500
    fivehundr = onethous%500
    twohund = fivehundr//200
    twohundr = fivehundr%200
    onehund = twohundr//100
    onehundr = twohundr%100
    fifty = onehundr//50
    fiftys = onehundr%50
    twe = fiftys//20
    twent = fiftys%20
    ten = twent//10
    tens = twent%10
    peso = tens//1
    pesos = tens%1
    print("Here is a breakdown, using Philippine denominition:")
    print(onethou,"-- 1000")
    print(fivehund,"-- 500")
    print(twohund,"-- 200")
    print(onehund,"-- 100")
    print(fifty,"-- 50")
    print(twe,"-- 20")
    print(ten,"-- 10")
    print(peso,"-- 1")

def code3():
    username = "Junior"
    password = "Good_B0y"

    import getpass
    while True: #To repeat the username until it's correct
        name = input("Enter your username: ")
        if name == username:
            print("Username Identified\n")
            break #Exit the loop
        else:
            print("Incorrect Username")
            print("Please Try Again\n")

    password1 = input("Enter your password:")
    if password1 == password:
        print("Access Complete")
    else:
        print("Access Denied")

def code4():
    number = int(input("Enter a number: "))

    if number % 2 == 0: #If your number divided into 2 it should have 0 remainder
        print("Even Number")

    else:
        print("Odd Numbers")

def code5():
    print("Welcome to Manga Recommendation!")
    print("Answer a few question to find your next read.")

    gen = input("What genre do you like? (action, romance, horror): ")

    #action
    if gen.lower() == "action":
        time = input("How long should the manga be? (short, medium, long): ")
        if time.lower() == "short":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tBlame! by Tsutomu Nihei \n\tDeadman Wonderland by Jinsei Kataoka")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tAoharu x Kikanjuu by NAOE \n\tAll You Need Is Kill by Ryōsuke Takeuchi")
        elif time.lower() == "medium":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tFreesia by Jiro Matsumoto \n\tKongō Banchō by Nakaba Suzuki")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tThe Violence Action Written by Shin Sawada, illustrated by Renji Asai \n\tChainsaw Man by Tatsuki Fujimoto")    
        elif time.lower() == "long":
            yr = input("Which decade? (2000s, 2010s): ")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tBlack Cat by Kentarou Yabuki \n\tSamurai Deeper Kyo by Akimine Kamijyo")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tAkame ga Kill! by Takahiro (story), Tetsuya Tashiro (art) \n\tHaikyu!! by Haruichi Furudate")    



    #romance
    if gen.lower() == "romance":
        time = input("How long should the manga be? (short, medium, long): ")
        if time.lower() == "short":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tLove Roma by Minoru Toyoda \n\tHoshi no Koe (Voices of a Distant Star) by Makoto Shinkai (story), Mizu Sahara (art)")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tSabaki No Mon (The Gates of Judgement) by Tsukuba Sakura \n\tHenshin Ganbou! Story: NISIO ISIN | Art: Miyokawa Masaru")
        elif time.lower() == "medium":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tKare Kano by Masami Tsuda \n\tDengeki Daisy by Kyousuke Motomi")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tKiss Me at the Stroke of Midnight by Rin Mikimoto \n\tKakafukaka by Takumi Ishida")    
        elif time.lower() == "long":
            yr = input("Which decade? (2000s, 2010s): ")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tSalad Days by Shinobu Inokuma \n\tSalad Days by Shinobu Inokuma")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tKaguya-sama: Love Is War by Aka Akasaka \n\tA Condition Called Love (Hananoi-kun to Koi no Yamai) by Megumi Morino")    

    #horror 
    if gen.lower() == "horror":
        time = input("How long should the manga be? (short, medium, long): ")
        if time.lower() == "short":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tHaunted House by Mitsukazu Mihara \n\tMantis Woman by Senno Knife")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tDissolving Classroom by Junji Ito \n\tBongcheon-Dong Ghost by Horang")
        elif time.lower() == "medium":
            yr = input("Which decade? (2000s, 2010s)")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tAnne Freaks by Yua Kotegawa \n\tSchool Zone by Kanako Inuki")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tCreature! by Shingo Honda \n\tHappiness by Shūzō Oshimi")    
        elif time.lower() == "long":
            yr = input("Which decade? (2000s, 2010s): ")
            if yr == "2000s":
                print("\nOur Manga Recommendation: \n\tDescendants of Darkness by Yoko Matsushita \n\tThe Kurosagi Corpse Delivery Service by Eiji Ōtsuka (story) and Housui Yamazaki (art)")
            elif yr == "2010s":
                print("\nOur Manga Recommendation: \n\tTokyo Ghoul by Sui Ishida  \n\tI Am a Hero by Kengo Hanazawa")    

    else:
        print("\n\tSorry but that genre isn't available. Please try again.")

def code6():
    num = eval(input("Enter a number: "))

    factorial = 1
    for x in range(num, 0, -1):
        factorial *= x 

    print("Factorial is ", factorial)

def code7():
    oddsum = 0

    for i in range(10):
        num = int(input("Enter a number: "))
        if num % 2 != 0:
            oddsum += num

    print("The sumation of all odd numbers is", oddsum)

def code8():
    print("MULTIPLACATION TABLE MAKER")
    num = eval(input("Enter a number: "))

    print(num)
    for i in range (1, 10+1):
        mul = num * i
        
        print(num, "x", i, "=", mul)

def code9():
    print("COUNTDOWN TIMER SIMULATOR")
    time = int(input("Enter the starting number for countdown:"))

    print("Countdown started:")
    for i in range (time, 0, -1):
        print(i)
    print("Liftoff!")

def code10():
    for outer in range(1,11,1):
        for kalso in range(10,outer,-1): # it will print reverse triangle 
            print(" ",end=" ") # but because of " " is will provide space/blank
        for inner in range(0,outer,1):
            print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()


def code11():
    # make a diamond using for loop

    #create triangle
    for outer in range(1,11,1):
        for kalso in range(10,outer,-1): # it will print reverse triangle 
            print(" ",end=" ") # but because of " " is will provide space/blank
        for inner in range(0,outer,1):
            print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    #reverse triangle
    for outer in range(9,0,-1):
        for kalso in range(10,outer,-1): # it will print reverse triangle 
            print(" ",end=" ") # but because of " " is will provide space/blank
        for inner in range(0,outer,1):
            print("*",end=" ") #therefore "*" is only visible, but it will print reverse because of kalso
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

def code12():
    for i in range(1,7,1):
        for kalso in range(7,i,-1):
            print(" ",end=" ")
        for s in range(i,0,-1):
            print(s,end=" ")
        for s in range(2,kalso,1):
            print(s,end=" ")
        print()

def code13():
    for outer in range(1,3,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("♦",end=" ") 
        for inner in range(1,outer,1):
            print("♦",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()
    for outer in range(3,0,-1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("♦",end=" ")
        for inner in range(1,outer,1):
            print("♦",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Big Triangle
    for outer in range(1,7,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("*",end=" ") 
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Big Triangle
    for outer in range(1,13,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("*",end=" ") 
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Big Triangle
    for outer in range(1,15,1):
        for kalso in range(15,outer,-1):
            print(" ",end=" ") 
        for inner in range(0,outer,1):
            print("*",end=" ") 
        for inner in range(1,outer,1):
            print("*",end=" ")
        for kalso in range(10,outer,-1):
            print(" ",end=" ")
        print()

    # Rectangle in the middle
    for outer in range(1,11,1):
        for kalso in range(11,1,-1):
            print(" ",end=" ") 
        for inner in range(0,9,1):
            print("+",end=" ") 
        print()


def code14():
    name = input("Enter your name: ")
    print("-"*40)
    odd = 0
    con = "" # Empty list
    proceed = True

    while proceed == True:
        num = eval(input("Enter a number: "))
        if num % 2 == 1: # to Identify if the number is Odd number
            print("Odd Detected")
            odd += num
            con += str(num) + "," # To concatenate all the odd number that the user enter
            continue
        elif num == 0: # Stop while the user input 0
            print("Loop Terminated")
            break
        else: # If the user enter a Even number
            print("Even detected")
            print("Skipping")
            continue

    print(f"Hi {name}, The sum of all the EVEN numbers is {odd}")
    print(f"All odd number: {con}")


def code15():
    # Anime list
    # Using list operations
    print("Anime Title List")

    anime_list = [] # empty list
    proceed = True   

    while proceed == True:
        anime = input("Enter the title of an Anime (or type 'end' to end): ")
        if anime == "end": # stopper
            print("All done,You are now exiting!! ")
            break    # terminate the loop

        else: # proceed
            print(f"'{anime}' added to the your Anime List") # every time that you answer, it will show up unless the user type "end"
            anime_list.append(anime) # all title that the user enter will be go to empty list

    print(f"Here All the Title of your Anime:") # after user type "end" it will show up
    for i in anime_list:     # print all the anime that the user enter
        print(f"- {i}")