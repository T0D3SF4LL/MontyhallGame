#include import module
import random
import time
text1="""Welcome to montyhall game"""
text2="This is an explanation about the game, please read all before the game!!!"
text3="""You've got three doors and these doors are A, B, C. There are two goats and one car behind doors 
by the way you have to make a choise from that doors """

print(text1)
time.sleep(0.7)
print("Loading game...")
time.sleep(3.0)

print(text3)
time.sleep(3.0)
#create doors list
doors=[]

#detect doors situations
situation1=['Auto','Goat','Goat']
situation2=['Goat','Auto','Goat']
situation3=['Goat','Goat','Auto']

# i am making some of situations
situations = [1,2,3]

# r is determined an item from situation list as random
r=random.choice(situations)

# get user input
choiseOfdoor=input("Now make your choice: (A, B or C): ").upper()
time.sleep(0.5)

# check and execute
if r==1:
    doors=situation1
    if choiseOfdoor=='A':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[-2])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
    elif choiseOfdoor=='B':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[-1])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
    elif choiseOfdoor=='C':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[-2])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
elif r==2:
    doors=situation2
    if choiseOfdoor=='A':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[-1])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
    elif choiseOfdoor=='B':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[2])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
    elif choiseOfdoor=='C':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[0])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
elif r==3:
    doors=situation3
    if choiseOfdoor=='A':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[1])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
    elif choiseOfdoor=='B':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[0])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
    if choiseOfdoor=='C':
        print("Nice one!\nI will remove one from other two doors ")
        del(doors[0])
        time.sleep(0.5)
        ask = input("Do you want to change your door ?(YES or NO) ").upper()
        if ask=='YES':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is B\nYou lose\nYou have got a GOAT :D")
        elif ask=='NO':
            print("waiting...")
            time.sleep(2.0)
            print("Your last door is A\nYou won!\nYou have got an AUTOMOBILE !!!")
else:
    print("NO GAME")