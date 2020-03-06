 #Game Code

#Import functions
import time
import random
import string
import sys

#Variable Setting
Difficulty = "Easy"
pg = 0
play = 0
modes = 4

#Setting variables
points = 0
lives = 2
naem = 0


#Easy Mode
def Eas():
    lives = 2
    points = 0
    if Difficulty == "Easy":
        while lives > 0:
            AN = ["Katy Perry", "Ariana Grande", "Ed Sheeran", "Michal Jackson", "Justin Bieber", "Taylor Swift", "Billie Eilish", "Beyonce", "Britney Spears", "Kesha"]
                
            #Songs By Artists
            KP = ["I Kissed A Girl", "Roar", "Last Friday Night", "Swish Swish", "Dark Horse", "Con Calma", "Fireworks", "California Girls"]
            AG = ["Side To Side", "Bang Bang", "Break Up With Your Girlfriend", "God Is A Woman", "Breathin", "Into You", "Seven Rings", "Needy"]
            ES = ["Shape Of You", "I Dont Care", "Thinking Out Loud", "Galway Girl", "Castle On The Hill", "Cross Me", "Happier", "Nancy Mulligan"]
            MJ = ["Smooth Criminal", "They Dont Care About Us", "Thriller", "Man In The Mirror", "Black Or White", "You Are Not Alone"]
            JB = ["What Do You Mean", "As Long As You Love", "Baby", "Sorry", "Never Say Never", "Beauty And The Beat"]
            TS = ["Shake It Off", "Look What You Made Me Do", "Bad Blood", "You Belong With Me", "Style", "Blank Space"]
            BE = ["Bad Guy", "All The Good Girls Go To Hell", "Idontwannabeyouanymore", "Wish You Were Gay", "I Love You", "You Should See Me Irl"]
            B = ["Halo", "Brown Skin Girl", "Crazy In Love", "Single Ladies", "If I Were A Boy", "Run The World"]
            BS = ["Toxic", "Baby One More Time", "Circus", "Im Not A Girl, Not Yet Anyways", "Womanizer", "Oops I Did It Again", "Work Bitch"]
            K = ["Tik Tok", "Die Young", "Take It Off", "True Colors", "Woman", "Your Love Is My Drug", "Blah Blah Blah", "Best Day"]

            rnd = random.choice(AN)

            print("\nYour first song is sung by " + rnd + ". The songs first letter is: ")
            time.sleep(1)

            if rnd == "Katy Perry":
                kpr = random.choice(KP)
                words = kpr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = kpr

            elif rnd == "Ariana Grande":
                agr = random.choice(AG)
                words = agr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = agr

            elif rnd == "Ed Sheeran":
                esr = random.choice(ES)
                words = esr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = esr

            elif rnd == "Michal Jackson":
                mjr = random.choice(MJ)        
                words = mjr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = mjr

            elif rnd == "Justin Bieber":
                jbr = random.choice(JB)
                words = jbr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = jbr

            elif rnd == "Taylor Swift":
                tsr = random.choice(TS)
                words = tsr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = tsr

            elif rnd == "Billie Eilish":
                ber = random.choice(BE)
                words = ber.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = ber

            elif rnd == "Beyonce":
                br = random.choice(B)
                words = br.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = br

            elif rnd == "Britney Spears":
                bsr = random.choice(BS)
                words = bsr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = bsr
                        
            elif rnd == "Kesha":
                kr = random.choice(K)
                words = kr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = kr

            time.sleep(1)
            answer = str(input("\nWhat song is this?   "))
            answer = string.capwords(answer)

            if answer == inp:
                time.sleep(1)
                print("You got it right! Congrats! \nYou have gotten +1 point!")
                points += 1
                time.sleep(.5)
                print("\nYour currently at " + str(points) + " points!")
                time.sleep(.5)
            else:
                time.sleep(1)
                print("\nIncorrect! You have lost a life!")
                time.sleep(.5)
                print("\nThe song was " + inp + ".")
                time.sleep(.5)
                lives -= 1
                        
            if lives == 0:
                time.sleep(1)
                print("\nYou have lost! It was a good run! You got " + str(points) + " points!")
                time.sleep(1)
                rb = input("Do you want to restart? (y/n)   ")
                rb = string.capwords(rb)
                if rb == "Y":
                    play = 0
                    time.sleep(1)
                    print("\nYou will now be sent back to the menu!")

                elif rb == "N":
                    print("Thats fine. Cya next time!")
                    sys.exit()

                else:
                    print("\nYour input was not valid, so we will assume you wanted to go back to the menu")
                    time.sleep(2)
                    play = 0



#HARD MODE
def Har():
    lives = 2
    points = 0
    if Difficulty == "Hard":
        while lives > 0:
            AN = ["Elvis Prezley", "Nicki Minaj", "Elton John", "Kanye West", "Dua Lipa", "Shawn Mendes", "Pink", "Paul McCartney", "Celine Dion", "Daddy Yankee"]
                    
            #Songs By Artists
            EP = ["Cant Help Falling In Love", "Love Me Tender", "Suspicious Minds", "Heartbreak Hotel", "All Shook Up", "Are You Lonesome Tonight"]
            NM = ["Bang Bang", "Super Bass", "Starships", "Good Form", "Right By My Side", "Truffle Butter", "Pills N Potions"]
            EJ = ["Im Still Standing", "Tiny Dancer", "Dont Go Breaking My Heart", "Rocket Man", "Bennie & The Jets", "Crockodile Rock"]
            KW = ["Gold Digger", "I Love It", "Flashing Lights", "Ni**as In Paris", "Jesus Walks", "All The Lights", "Mercy", "Cant Tell Me Nothing"]
            DL = ["No Lie", "Hotter Than Hell", "Swan Song", "Thinking Bout You", "Scared To Be Lonely", "Lost In Your Light", "Be The One"]
            SM = ["Senorita", "Treat You Better", "Nervous", "Fallin All In You", "I Know What You Did", "Lost In Japan", "In My Blood"]
            P = ["Just Give Me A Reason", "Walk Me Home", "Try", "Just Like Fire", "What About Us", "Fuckin Perfect", "Can We Pretend", "Blow Me"]
            PM = ["Hey Jude", "Ob-La-Di, Ob-La-Da", "Yesterday", "Yellow Submarine", "I Want To Hold Your Hand", "Eleanor Rigby", "Twist And Shout"]
            CD = ["My Heart Will Go On", "Think Twice", " A New Day Has Come", "Immortality", "Im Your Angel", "I Drove All Night", "Just Walk Away"]
            DY = ["Con Calma", "China", "Dura", "No Lo Trates", "Si Supieras", "Shaky Shaky", "Sommos De Calle", "Gasolina", "Limbo", "Runaway"]

            rnd = random.choice(AN)

            print("\nYour first song is sung by " + rnd + ". The songs first letter is: ")
            time.sleep(1)

            if rnd == "Elvis Prezley":
                epr = random.choice(EP)
                words = epr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = epr

            elif rnd == "Nicki Minaj":
                nmr = random.choice(NM)
                words = nmr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = nmr

            elif rnd == "Elton John":
                ejr = random.choice(EJ)
                words = ejr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = ejr

            elif rnd == "Kanye West":
                kwr = random.choice(KW)
                words = kwr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = kwr

            elif rnd == "Dua Lipa":
                dlr = random.choice(DL)
                words = dlr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = dlr

            elif rnd == "Shawn Mendes":
                smr = random.choice(SM)
                words = smr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = smr

            elif rnd == "Pink":
                pr = random.choice(P)
                words = pr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = pr

            elif rnd == "Paul McCartney":
                pmr = random.choice(PM)
                words = pmr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = pmr

            elif rnd == "Celine Dion":
                cdr = random.choice(CD)
                words = cdr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = cdr
                            
            elif rnd == "Daddy Yankee":
                dyr = random.choice(DY)
                words = dyr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = dyr

            time.sleep(1)
            answer = str(input("\nWhat song is this?   "))
            answer = string.capwords(answer)

            if answer == inp:
                time.sleep(1)
                print("You got it right! Congrats! \nYou have gotten +1 point!")
                points += 1
                time.sleep(.5)
                print("\nYour currently at " + str(points) + " points!")
                time.sleep(.5)
            else:
                time.sleep(1)
                print("\nIncorrect! You have lost a life!")
                time.sleep(.5)
                print("\nThe song was " + inp + ".")
                time.sleep(.5)
                lives -= 1
                        
            if lives == 0:
                time.sleep(1)
                print("\nYou have lost! It was a good run! You got " + str(points) + " points!")
                time.sleep(1)
                rb = input("Do you want to restart? (y/n)   ")
                rb = string.capwords(rb)
                if rb == "Y":
                    play = 0
                    time.sleep(1)
                    print("\nYou will now be sent back to the menu!")

                elif rb == "N":
                    print("Thats fine. Cya next time!")
                    sys.exit()

                else:
                    print("\nYour input was not valid, so we will assume you wanted to go back to the menu")
                    time.sleep(2)
                    play = 0



#Isaac Mode
def Issa():
    lives = 2
    points = 0
    if Difficulty == "Isaac":
        while lives > 0:
            AN = ["Destiny 2", "Star Wars", "Pirates Of The Caribbean", "Halo", "Read Dead Redemption"]
                    
            #Songs By Artists
            DT = ["Inner Light", "Last Rite", "Rise", "Towerfall", "Lost Light", "Forge Ahead", "Battle station"]
            SW = ["Starwars Theme", "Cantina Band", "Binary Sunset", "The Hologram", "Imperial Attack", "The Trash Compactor", "The Battle Of Yavin"]
            POTC = ["Fog Bound", "The Medallion Calls", "The Black Pearl", "Will And Elizabeth", "Swords Crossed", "Walk The Plank"]
            H = ["Halo Original Soundtrack"]
            RDR = ["Deadmans Gun", "Far Away", "Gunplay", "Born Unto Trouble", "The Shootist", "Already Dead", "Horseplay", "Exodus In America"]
                    

            rnd = random.choice(AN)

            print("\nYour first song is from " + rnd + ". The songs first letter is: ")
            time.sleep(1)

            if rnd == "Destiny 2":
                dtr = random.choice(DT)
                words = dtr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = dtr

            elif rnd == "Star Wars":
                swr = random.choice(SW)
                words = swr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = swr

            elif rnd == "Pirates Of The Caribbean":
                potcr = random.choice(POTC)
                words = potcr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = potcr

            elif rnd == "Halo":
                hr = random.choice(H)
                words = hr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = hr

            elif rnd == "Read Dead Redemption":
                rdrr = random.choice(RDR)
                words = rdrr.split()
                letters = [word[0] for word in words]
                print(" ".join(letters))
                inp = rdrr
                        
            time.sleep(1)
            answer = str(input("\nWhat song is this?   "))
            answer = string.capwords(answer)

            if answer == inp:
                time.sleep(1)
                print("You got it right! Congrats! \nYou have gotten +1 point!")
                points += 1
                time.sleep(.5)
                print("\nYour currently at " + str(points) + " points!")
                time.sleep(.5)
            else:
                time.sleep(1)
                print("\nIncorrect! You have lost a life!")
                time.sleep(.5)
                print("\nThe song was " + inp + ".")
                time.sleep(.5)
                lives -= 1
                    
            if lives == 0:
                time.sleep(1)
                print("\nYou have lost! It was a good run! You got " + str(points) + " points!")
                time.sleep(1)
                rb = input("Do you want to restart? (y/n)   ")
                rb = string.capwords(rb)
                if rb == "Y":
                    play = 0
                    time.sleep(1)
                    print("\nYou will now be sent back to the menu!")

                elif rb == "N":
                    print("Thats fine. Cya next time!")
                    sys.exit()

                else:
                    print("\nYour input was not valid, so we will assume you wanted to go back to the menu")
                    time.sleep(2)
                    play = 0
                    
def Ani():
    lives = 2
    points = 0
    if Difficulty == "AnimeHard":
        while lives > 0:
            AN = ["Sword Art Online", "My Hero Academia", "Tokyo Ghoul", "One Punch Man", "Your Lie In April", "Dragon Ball", "Yuri On Ice", "Pokemon", "Naruto", "Neon Genesis", "Death Note", "Fullmetal ALchemist"]
                
            #Songs By Artists
            SAO = "people getting stuck in a VR game, where if they die there they die in real life."
            MHA = "people are born with abilities called Quirks that allow people to beat villains."
            TG = "society is split into two where a new breed of humans that feest upon humans named ghouls fight those who oppose them."
            OPM = "a bald guy trains so hard he can kill every villain with only one punch."
            YLIA = "man who has lost passion for piano gets his passion reignited after meeting a violinist."
            DB = "icredibly strong kid with tail goes on adventures with a midget bald kid and a pedophilic master."
            YOI = "gay guys ice-skate together to climb the leaderboards."
            P = "kid who dreams of being the best ventures with two friends to capture and befriend animals."
            N = "guy spams shurikens at bad guys whilst doing a bunch of weird hand signs and wearing a cool headband."
            NG = "people who can pilot big machines fight aliens called angels to regain control of the earth."
            DN = "guy with notebook kills people to cleanse the world."
            FA = "two siblings who lost their mum in an alchemy involved experiment, persue their passion as state alchemist and fight bad guys."
            

            ANR = random.choice(AN)
            words = ANR.split()
            letters = [word[0] for word in words]
            print("The initials for the anime are:")
            print(" ".join(letters))

            if ANR == "Sword Art Online":
                print("\nThe first anime is about " + SAO)

            elif ANR == "My Hero Academia":
                print("\nThe first anime is about " + MHA)

            elif ANR == "Tokyo Ghoul":
                print("\nThe first anime is about " + TG)

            elif ANR == "One Punch Man":
                print("\nThe first anime is about " + OPM)

            elif ANR == "Your Lie In April":
                print("\nThe first anime is about " + YLIA)

            elif ANR == "Dragon Ball":
                print("\nThe first anime is about " + DB)

            elif ANR == "Yuri On Ice":
                print("\nThe first anime is about " + YOI)

            elif ANR == "Pokemon":
                print("\nThe first anime is about " + P)

            elif ANR == "Naruto":
                print("\nThe first anime is about " + N)

            elif ANR == "Neon Genesis":
                print("\nThe first anime is about " + NG)

            elif ANR == "Death Note":
                print("\nThe first anime is about " + DN)

            elif ANR == "Fullmetal Alchemist":
                print("\nThe first anime is about " + FA)
                
            


            time.sleep(1)
            answer = str(input("\nWhat Anime is this?   "))
            answer = string.capwords(answer)

            if answer == ANR:
                time.sleep(1)
                print("You got it right! Congrats! \nYou have gotten +1 point!")
                points += 1
                time.sleep(.5)
                print("\nYour currently at " + str(points) + " points!")
                time.sleep(.5)
            else:
                time.sleep(1)
                print("\nIncorrect! You have lost a life!")
                time.sleep(.5)
                print("\nThe anime was " + ANR + ".")
                time.sleep(.5)
                lives -= 1
                        
            if lives == 0:
                time.sleep(1)
                print("\nYou have lost! It was a good run! You got " + str(points) + " points!")
                time.sleep(1)
                rb = input("Do you want to restart? (y/n)   ")
                rb = string.capwords(rb)
                if rb == "Y":
                    play = 0
                    time.sleep(1)
                    print("\nYou will now be sent back to the menu!")

                elif rb == "N":
                    print("Thats fine. Cya next time!")
                    sys.exit()

                else:
                    print("\nYour input was not valid, so we will assume you wanted to go back to the menu")
                    time.sleep(2)
                    play = 0


def AniH():
    lives = 2
    points = 0
    if Difficulty == "AnimeHard":
        while lives > 0:
            AN = ["Guilty Crown", "Norogami", "Kakeguri", "Mob Psycho 100", "Love Live", "Revisions", "Eromanga Sensei", "Baki", "Island", "Darling In The Franxxx", "Highschool Of The Dead", "The Hero Is Overpowered But Overly Cautious", "Konosuba", "Dragon Pilot", "Ouran Highschool Host Club"]
                
            #Songs By Artists
            GC = "guy can rip out weapons allocating with their personality out of their chest, sometimes rendering them immobilised."
            N = "god grants peoples wishes for only 5 yen whilst using a spirit as a weapon."
            K = "people obsesed with gambling revolve their whole school life over it, where status is everything."
            MP = "a natural born psychych 'melts' ghosts with his mentor being a con artist, abusing his disciple for his sake."
            LL = "band of girls sing and dance gaining the attention of millions, whilst having to deal with their personal life as well."
            R = "massive robot monsters from the future attack civilisation, and only a group of children can stop them."
            ES = "siblings help each other make a popular web series without knowing each others identity."
            B = "men fight to the death trying to decide who is the strongest."
            I = "criminals who had their minds wiped get stuck on an island, depretaly trying to escape."
            DITF = "evangelion buty better, and being a darling is normal."
            HOTD = "a virus breaks out, killing most of the population, but a group of highschool students survive."
            THIOBOC = "guy is overpowered, but extremely cautious to the point that he can 1 shot everyone, but doesnt want to"
            KO = "guy dies whilst trying to save a girl not in danger, then gets teleported to an alternate world with the godess who made fun of him"
            DP = "people ride dragons who can turn into fighter jets, so they use these dragons to fight and protect their country."
            DP = "people ride dragons who can turn into fighter jets, so they use these dragons to fight and protect their country."
            OHHC = "basic slice of life set in a highschool based on love"

            ANR = random.choice(AN)
            words = ANR.split()
            letters = [word[0] for word in words]
            print("The initials for the anime are:")
            print(" ".join(letters))

            if ANR == "Guilty Crown":
                print("\nThe first anime is about " + GC)

            elif ANR == "Norogami":
                print("\nThe first anime is about " + N)

            elif ANR == "Kakeguri":
                print("\nThe first anime is about " + K)

            elif ANR == "Mob Psycho 100":
                print("\nThe first anime is about " + MP)

            elif ANR == "Love Live":
                print("\nThe first anime is about " + LL)

            elif ANR == "Revisions":
                print("\nThe first anime is about " + R)

            elif ANR == "Eromanga Sensei":
                print("\nThe first anime is about " + ES)

            elif ANR == "Baki":
                print("\nThe first anime is about " + B)

            elif ANR == "Island":
                print("\nThe first anime is about " + I)

            elif ANR == "Darling In The Franxxx":
                print("\nThe first anime is about " + DITF)

            elif ANR == "Highschool Of The Dead":
                print("\nThe first anime is about " + HOTD)
                
            elif ANR == "The Hero Is Overpowered But Overly Cautious":
                print("\nThe first anime is about " + THIOBOC)

            elif ANR == "Konosuba":
                print("\nThe first anime is about " + KO)

            elif ANR == "Dragon Pilot":
                print("\nThe first anime is about " + DP)

            elif ANR == "Ouran Highschool Host Club":
                print("\nThe first anime is about " + OHHC)
                
            


            time.sleep(1)
            answer = str(input("\nWhat Anime is this?   "))
            answer = string.capwords(answer)

            if answer == ANR:
                time.sleep(1)
                print("You got it right! Congrats! \nYou have gotten +1 point!")
                points += 1
                time.sleep(.5)
                print("\nYour currently at " + str(points) + " points!")
                time.sleep(.5)
            else:
                time.sleep(1)
                print("\nIncorrect! You have lost a life!")
                time.sleep(.5)
                print("\nThe anime was " + ANR + ".")
                time.sleep(.5)
                lives -= 1
                        
            if lives == 0:
                time.sleep(1)
                print("\nYou have lost! It was a good run! You got " + str(points) + " points!")
                time.sleep(1)
                rb = input("Do you want to restart? (y/n)   ")
                rb = string.capwords(rb)
                if rb == "Y":
                    play = 0
                    time.sleep(1)
                    print("\nYou will now be sent back to the menu!")

                elif rb == "N":
                    print("Thats fine. Cya next time!")
                    sys.exit()

                else:
                    print("\nYour input was not valid, so we will assume you wanted to go back to the menu")
                    time.sleep(2)
                    play = 0


#Sub-routine for restart
def answerr():
    dswg = input("\nDo you want to start the game? (y/n)    ")

    dswg = string.capwords(dswg)
    if dswg == "Y":
        time.sleep(1)
        print("\nThe game will now begin!")
        play = 1
                        
    elif dswg == "N":
        time.sleep(1)
        print("\nOk, we will now send you to the menu")


    else:
        print("Your input was not valid, so we will assume you wanted to go back to the menu")
        time.sleep(1)
        print("\You are being transported now.")
        play = 1
        naem = 1
        time.sleep(1)

#Whole programme restart
while pg == 0:

    #Menu script
    while play == 0:
        
        #Introduction and name data gathering
        if naem == 1:
            print("Hello, and welcome to Kai's music game!")
            time.sleep(1)
            if name == "Test":
                name = "Jakub"
            
            print("Hi " + name)
            print("")
            time.sleep(.10)

        #Welcoming
        elif naem == 0:
            print("Hello, and welcome to Kai's music game!")
            time.sleep(1)
            print("What is your name?")
            name = input("")
            name = string.capwords(name)
            print("Hi " + name)
            if name == "Isaac":
                time.sleep(.10)
                print("")
                Difficulty = "Isaac"
                print("")
                time.sleep(.10)

            #Behind the scenes testing
            elif name == "Test":
                time.sleep(.10)
                print("What do you want to test?")
                time.sleep(.10)
                print("Easy (1)")
                time.sleep(.10)
                print("Hard (2)")
                time.sleep(.10)
                print("Isaac (3)")
                time.sleep(.10)
                print("Anime (4)")
                time.sleep(.10)
                print("Anime Hard (5)")
                time.sleep(.10)
                test = input("")

                #Mode Setting behind the scenes
                if test == "1":
                    play = 1
                    Difficulty = "Easy"
                    Eas()
                    
                elif test == "2":
                    play = 1
                    Difficulty = "Hard"
                    Har()

                elif test == "3":
                    play = 1
                    Difficulty = "Isaac"
                    Issa()

                elif test == "4":
                    play = 1
                    Difficulty = "Anime"
                    Ani()

                elif test == "5":
                    play = 1
                    Difficulty = "AnimeHard"
                    AniH()
                
                print("")
                time.sleep(.10)

            #Joke
            elif name == "Jakub":
                print("")
                time.sleep(.10)
                print("No its not. I never use my name. Ever.")
                print("")
                time.sleep(.10)
        
        #Main menu
        time.sleep(1)
        print("\nYour current difficulty is " + str(Difficulty))
        time.sleep(1)
        print("\n-Play-")
        time.sleep(.10)
        print("-Rules-")
        time.sleep(.10)
        print("-Modes-")
        time.sleep(.10)
        print("-Quit-")
        ip = str(input("\n"))
        time.sleep(1)
        ip = string.capwords(ip)

        #Start of Game
        if ip == "Play":
            print("The game will now begin!")
            play = 1

        #Explains Rules
        elif ip == "Rules":
            print("\n------ Rules ------")
            time.sleep(.5)
            print("\nThe rules of my game")
            time.sleep(.5)
            print("are simple, you will be")
            time.sleep(.5)
            print("given the name of music")
            time.sleep(.5)
            print("authors and the beggining")
            time.sleep(.5)
            print("letters of one of their")
            time.sleep(.5)
            print("songs. You will have two")
            time.sleep(.5)
            print("attempts and will get more")
            time.sleep(.5)
            print("points depending how many")
            time.sleep(.5)
            print("attempts you use up.")
            time.sleep(5)

            answerr()

        #Set Mode
        elif ip == "Modes":
            print("\nWe currently have " + str(modes) + " modes. They are:")
            time.sleep(.10)
            print("\nEasy (1)")
            time.sleep(.10)
            print("Hard (2)")
            time.sleep(.10)
            print("Anime (3)")
            time.sleep(.10)
            print("Anime HARD (4)")
            mAN = input("")

            if mAN == "1":
                time.sleep(.10)
                print("The mode will now be set to easy. Sending you back to the menu...")
                time.sleep(.10)
                print("")
                Difficulty = "Easy"
                print("")
                time.sleep(.10)
                play = 0
                naem = 1


            elif mAN == "2":
                time.sleep(.10)
                print("The mode will now be set to hard. Sending you back to the menu...")
                time.sleep(.10)
                print("")
                Difficulty = "Hard"
                print("")
                time.sleep(.10)
                play = 0
                naem = 1

            elif mAN == "3":
                time.sleep(.10)
                print("The mode will now be set to anime. Sending you back to the menu...")
                time.sleep(.10)
                print("")
                Difficulty = "Anime"
                print("")
                time.sleep(.10)
                play = 0
                naem = 1

            elif mAN == "4":
                time.sleep(.10)
                print("The mode will now be set to anime hard. Sending you back to the menu...")
                time.sleep(.10)
                print("")
                Difficulty = "Anime Hard"
                print("")
                time.sleep(.10)
                play = 0
                naem = 1

                

            else:
                print("Your input was not valid...")
                answerr()
                print("")
        
        #Quit
        elif ip == "Quit":
            sys.exit()

        else:
            print("Your input was not valid, so we will assume you wanted to start the game")
            time.sleep(2)
            print("\nThe game will now begin!")
            play = 1

    #Song Authors
    while lives > 0:
        Eas()
        Har()
        Issa()
        Ani()
        AniH()






    


