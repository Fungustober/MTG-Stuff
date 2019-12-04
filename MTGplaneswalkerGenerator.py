#------------------------------------
#Magic: The Gathering Planeswalker Generator
#------------------------------------
#Created by Ben Buehler (Do not remove)
#------------------------------------
#Modified by (Your name here if modifying)
#------------------------------------
#Purpose: to allow people to easily create Planeswalkers from MTG through random generation.
#------------------------------------
#Copyright Notice:
#
#This is open source code. You can use it to your heart's content. However, if modifying it, you must 
#state that this was modified by you and not made by you by writing your name or screen name next to 
#the "Modified by" section. You can copy and paste the "Modified by" section if you are modifying an 
#already modified version of this. If you have modified this, and you wish to distribute this for others to modify, please be 
#kind and copy paste the "Modified by" section.
#------------------------------------
#Probability:
#
#    # of races = 39
#    # of gender categories = 3
#    # of color combinations = 31
# 39*3 = 114
# 114*31 = 3,534
# There are 3,534 possible outcomes.
# If a unique(not a repeat of previous outcomes) planeswalker was generated every second, 
# it would take 58 minutes and 54 seconds for all of them to generate.
#------------------------------------
import random
def main():
    ans = ""
    charNum = getCharNum()
    for count in range(charNum):
        race = charRace()
        gender = charGender()
        colors = colorGen()
        print("Character", count+1, "is a", gender, race, "who uses the color(s)", colors, "for magic.")
    ans = input("Would you like to create another random set of characters? Yes/No ")
    while ans == "Yes" or ans == "yes" or ans == "y" or ans == "Y":
        count = 0
        charNum = getCharNum()
        for count in range(charNum):
            race = charRace()
            gender = charGender()
            colors = colorGen()
            print("Character", count+1, "is a", gender, race, "who uses the color(s)", colors, "for magic.")
        ans = input("Would you like to create another random set of characters? Yes/No ")

def getCharNum():
    charNum = int(input("Enter the number of planeswalkers you want: "))
    while charNum < 1:
        charNum = int(input("ERROR: Number of planeswalkers cannot be less than 1! Please enter the number of planeswalkers you want:"))
    return charNum

def charRace():
    race = ""
    raceInt = random.randint(1,96)
    if raceInt == 1:
        race = "Aven"
    elif raceInt == 2:
        race = "Azra"
    elif raceInt == 3:
        race = "Centaur"
    elif raceInt == 4:
        race = "Cyclops"
    elif raceInt >= 5 and raceInt <= 7:
        race = "Dryad"
    elif raceInt == 8:
        race = "Dwarf"
    elif raceInt >= 9 and raceInt <= 12:
        race = "Elf"
    elif raceInt >= 13 and raceInt <= 15:
        race = "Fae"
    elif raceInt == 16:
        race = "Giant"
    elif raceInt >= 17 and raceInt <= 19:
        race = "Goblin"
    elif raceInt >= 20 and raceInt <= 22:
        race = "Gorgon"
    elif raceInt == 23:
        race = "Khenra"
    elif raceInt == 24:
        race = "Kithkin"
    elif raceInt == 25:
        race = "Kobold"
    elif raceInt >= 26 and raceInt <= 28:
        race = "Kor"
    elif raceInt == 29:
        race = "Kraul"
    elif raceInt >= 30 and raceInt <= 32:
        race = "Leonin"
    elif raceInt == 33:
        race = "Loxodon"
    elif raceInt >= 34 and raceInt <= 36:
        race = "Merfolk"
    elif raceInt >= 37 and raceInt <= 39:
        race = "Minotaur"
    elif raceInt >= 40 and raceInt <= 42:
        race = "Moonfolk"
    elif raceInt == 43:
        race = "Naga"
    elif raceInt == 44:
        race = "Ogre"
    elif raceInt == 45:
        race = "Orc"
    elif raceInt == 46:
        race = "Ouphe"
    elif raceInt == 47:
        race = "Rhox"
    elif raceInt >= 48 and raceInt <= 50:
        race = "Satyr"
    elif raceInt == 51:
        race = "Siren"
    elif raceInt >= 52 and raceInt <= 54:
        race = "Vedalken"
    elif raceInt == 55 or raceInt == 56:
        race = "Viashino"
    elif raceInt >= 57 and raceInt <= 59:
        race = "Werewolf"
    elif raceInt >= 60 and raceInt <= 62:
        race = "Pantherfolk"
    elif raceInt == 63:
        race = "Ainok"
    elif raceInt == 64:
        race = "Amphin"
    elif raceInt == 65:
        race = "Kitsune"
    elif raceInt == 66:
        race = "Nantuko"
    elif raceInt == 67:
        race = "Nezumi"
    elif raceInt == 68:
        race = "Orochi"
    elif raceInt >= 69 and raceInt <= 96:
        race = "Human"
    return race

def charGender():
    gender =""
    genderInt = random.randint(1, 7)
    if genderInt >=1 and genderInt <= 3:
        gender = "Male"
    elif genderInt >=4 and genderInt <= 6:
        gender = "Female"
    elif genderInt ==7:
        gender = "Non-Binary"
    return gender

def colorGen():
    color = ""
    colorInt = random.randint(1,127)
    if colorInt == 1:
        color = "White, Blue, Black, Red, and Green (All colors)"
    elif colorInt >= 2 and colorInt <= 3:
        color = "White, Blue, Black, and Red"
    elif colorInt >= 4 and colorInt <= 5:
        color = "Blue, Black, Red, and Green"
    elif colorInt >= 6 and colorInt <= 7:
        color = "Black, Red, Green, and White"
    elif colorInt >= 8 and colorInt <= 9:
        color = "Red, Green, White, and Blue"
    elif colorInt >= 10 and colorInt <= 11:
        color = "Green, White, Blue, and Black"
    elif colorInt >= 12 and colorInt <= 15:
        color = "White, Blue, and Black"
    elif colorInt >= 16 and colorInt <= 18:
        color = "Blue, Black, and Red"
    elif colorInt >= 19 and colorInt <= 21:
        color = "Black, Red, and Green"
    elif colorInt >= 22 and colorInt <= 24:
        color = "Red, Green, and White"
    elif colorInt >= 25 and colorInt <= 27:
        color = "Green, White, and Blue"
    elif colorInt >= 28 and colorInt <= 30:
        color = "White, Red, and Black"
    elif colorInt >= 31 and colorInt <= 33:
        color = "Blue, Red, and Green"
    elif colorInt >= 34 and colorInt <= 36:
        color = "Black, White, and Green"
    elif colorInt >= 37 and colorInt <= 39:
        color = "Red, Blue, and White"
    elif colorInt >= 40 and colorInt <= 42:
        color = "Green, Blue, and Black"
    elif colorInt >= 43 and colorInt <= 47:
        color = "White"
    elif colorInt >= 48 and colorInt <= 52:
        color = "Blue"
    elif colorInt >= 53 and colorInt <= 57:
        color = "Black"
    elif colorInt >= 58 and colorInt <= 62:
        color = "Red"
    elif colorInt >= 63 and colorInt <= 67:
        color = "Green"
    elif colorInt >= 68 and colorInt <= 73:
        color = "White and Blue"
    elif colorInt >= 74 and colorInt <= 79:
        color = "Blue and Black"
    elif colorInt >= 80 and colorInt <= 85:
        color = "Black and Red"
    elif colorInt >= 86 and colorInt <= 91:
        color = "Red and Green"
    elif colorInt >= 92 and colorInt <= 97:
        color = "Green and White"
    elif colorInt >= 98 and colorInt <= 103:
        color = "White and Black"
    elif colorInt >= 104 and colorInt <= 109:
        color = "White and Red"
    elif colorInt >= 110 and colorInt <= 115:
        color = "Blue and Red"
    elif colorInt >= 116 and colorInt <= 121:
        color = "Blue and Green"
    elif colorInt >= 122 and colorInt <= 127:
        color = "Black and Green"
    return color

main()