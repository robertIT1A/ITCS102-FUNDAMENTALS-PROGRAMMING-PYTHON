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
