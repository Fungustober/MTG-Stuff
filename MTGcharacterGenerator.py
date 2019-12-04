#------------------------------------
#Magic: The Gathering Character Generator
#------------------------------------
#Created by Ben Buehler (Do not remove)
#------------------------------------
#Modified by (Your name here if modifying)
#------------------------------------
#Purpose: to allow people to easily create MTG characters through random generation.
#------------------------------------
#Copyright Notice:
#
#This is open source code. You can use it to your heart's content. However, if modifying it, you must 
#state that this was modified by you and not made by you by writing your name or screen name next to 
#the "Modified by" section. You can copy and paste the "Modified by" section if you are modifying an 
#already modified version of this. If you have modified this, and you wish to distribute this for others to modify, please be 
#kind and copy paste the "Modified by" section.
#------------------------------------
#Possible Outcomes:
#
#    # of races = 67
#    # of classes = 43
#    # of outcomes for extra classes/races = 4 (outcome 1: Neither, Outcome 2: Both, Outcome 3: Extra Race, Outcome 4: Extra Classes)
#       # of races = 67
#       # of classes = 43
#    # of gender categories = 3
#    # of color combinations = 31
# 67*43 = 2,881
# outcome 2: 2,881; Outcome 3: 67; Outcome 4: 43; thus 2,881*67 = 193,027*43 = 8,300,161
# 8,300,161*2,881 = 23,912,763,841
# 23,912,763,841*3 = 71,738,291,523
# 71,738,291,523*31 = 2,223,887,037,210
# There are 2,223,887,037,210 possible outcomes.
# If a unique(not a repeat of previous outcomes) character was generated every second, 
# it would take 70,518 years and 30 seconds for all of them to generate.
#------------------------------------
import random
def main():
    charNum = getNum()
    for num in range(charNum):
        sClassB = calc()
        sCharB = calc()
        if sClassB == True and sCharB == True:
            gender = charGender()
            race = charRace()
            raceT =charRace()
            charClass = getCharClass()
            charClassT = getCharClass()
            colors = getColors()
            print("Character", num+1, "is a", gender, race, raceT, charClass, charClassT, "who uses the color(s)", colors, "for magic.")
        elif sClassB == True:
            gender = charGender()
            race = charRace()
            charClass = getCharClass()
            charClassT = getCharClass()
            colors = getColors()
            print("Character", num+1, "is a", gender, race, charClass, charClassT, "who uses the color(s)", colors, "for magic.")
        elif sCharB == True:
            gender = charGender()
            race = charRace()
            raceT =charRace()
            charClass = getCharClass()
            charClassT = getCharClass()
            colors = getColors()
            print("Character", num+1, "is a", gender, race, raceT, charClass,"who uses the color(s)", colors, "for magic.")
        else:
            gender = charGender()
            race = charRace()
            charClass = getCharClass()
            colors = getColors()
            print("Character", num+1, "is a", gender, race, charClass, "who uses the color(s)", colors, "for magic.")
    ans = input("Would you like to generate more characters? Yes/No ")
    while ans == "Yes" or ans == "yes":
        charNum = getNum()
        for num in range(charNum):
            sClassB = calc()
            sCharB = calc()
            if sClassB == True and sCharB == True:
                gender = charGender()
                race = charRace()
                raceT =charRace()
                charClass = getCharClass()
                charClassT = getCharClass()
                colors = getColors()
                print("Character", num+1, "is a", gender, race, raceT, charClass, charClassT, "who uses the color(s)", colors, "for magic.")
            elif sClassB == True:
                gender = charGender()
                race = charRace()
                charClass = getCharClass()
                charClassT = getCharClass()
                colors = getColors()
                print("Character", num+1, "is a", gender, race, charClass, charClassT, "who uses the color(s)", colors, "for magic.")
            elif sCharB == True:
                gender = charGender()
                race = charRace()
                raceT =charRace()
                charClass = getCharClass()
                charClassT = getCharClass()
                colors = getColors()
                print("Character", num+1, "is a", gender, race, raceT, charClass,"who uses the color(s)", colors, "for magic.")
            else:
                gender = charGender()
                race = charRace()
                charClass = getCharClass()
                colors = getColors()
                print("Character", num+1, "is a", gender, race, charClass, "who uses the color(s)", colors, "for magic.")
        ans = input("Would you like to generate more characters? Yes/No ")

def getNum():
    num = int(input("Enter the amount of characters you would like to generate: "))
    while num < 1:
        num = int(input("ERROR: number cannot be less than 1. Please try again: "))
    return num

def charRace():
    race = ""
    raceInt = random.randint(1,67)
    if raceInt == 1:
        race = "Ape"
    elif raceInt == 2:
        race = "Azra"
    elif raceInt == 3:
        race = "Centaur"
    elif raceInt == 4:
        race = "Cyclops"
    elif raceInt == 5:
        race = "Dauthi"
    elif raceInt == 6:
        race = "Dryad"
    elif raceInt == 7:
        race = "Dwarf"
    elif raceInt == 8:
        race = "Elf"
    elif raceInt == 9:
        race = "Faefolk"
    elif raceInt == 10:
        race = "Giant"
    elif raceInt == 11:
        race = "Gnome"
    elif raceInt == 12:
        race = "Goblin"
    elif raceInt == 13:
        race = "Gorgon"
    elif raceInt == 14:
        race = "Hag"
    elif raceInt == 15:
        race = "Human"
    elif raceInt == 16:
        race = "Kithkin"
    elif raceInt == 17:
        race = "Kobold"
    elif raceInt == 18:
        race = "Kor"
    elif raceInt == 19:
        race = "Merfolk"
    elif raceInt == 20:
        race = "Minotaur"
    elif raceInt == 21:
        race = "Moonfolk"
    elif raceInt == 22:
        race = "Naga"
    elif raceInt == 23:
        race = "Ogre"
    elif raceInt == 24:
        race = "Orc"
    elif raceInt == 25:
        race = "Ouphe"
    elif raceInt == 26:
        race = "Satyr"
    elif raceInt == 27:
        race = "Siren"
    elif raceInt == 28:
        race = "Surrakar"
    elif raceInt == 29:
        race = "Troll"
    elif raceInt == 30:
        race = "Vedalken"
    elif raceInt == 31:
        race = "Viashino"
    elif raceInt == 32:
        race = "Werewolf"
    elif raceInt == 33:
        race = "Ainok"
    elif raceInt == 34:
        race = "Amphin"
    elif raceInt == 35:
        race = "Aven"
    elif raceInt == 36:
        race = "Khenra"
    elif raceInt == 37:
        race = "Kitsune"
    elif raceInt == 38:
        race = "Kraul"
    elif raceInt == 39:
        race = "Leonin"
    elif raceInt == 40:
        race = "Loxodon"
    elif raceInt == 41:
        race = "Nantuko"
    elif raceInt == 42:
        race = "Nezumi"
    elif raceInt == 43:
        race = "Orochi"
    elif raceInt == 44:
        race = "Rhox"
    elif raceInt == 45:
        race = "Wolfir"
    elif raceInt == 46:
        race = "Aetherborn"
    elif raceInt == 47:
        race = "Angel"
    elif raceInt == 48:
        race = "Avatar"
    elif raceInt == 49:
        race = "Nymph"
    elif raceInt == 50:
        race = "Shapeshifter"
    elif raceInt == 51:
        race = "Vampire"
    elif raceInt == 52:
        race = "Cephalid"
    elif raceInt == 53:
        race = "Demon"
    elif raceInt == 54:
        race = "Dragon"
    elif raceInt == 55:
        race = "Elemental"
    elif raceInt == 56:
        race = "Eye"
    elif raceInt == 57:
        race = "Gremlin"
    elif raceInt == 58:
        race = "Homarid"
    elif raceInt == 59:
        race = "Homunculus"
    elif raceInt == 60:
        race = "Incarnation"
    elif raceInt == 61:
        race = "Sphinx"
    elif raceInt == 62:
        race = "Thallid"
    elif raceInt == 63:
        race = "Treefolk"
    elif raceInt == 64:
        race = "Camarid"
    elif raceInt == 65:
        race = "Licid"
    elif raceInt == 66:
        race = "Scarecrow"
    elif raceInt == 67:
        race = "Myr"
    return race

def calc():
    dec = False
    num = random.randint(1,20)
    if num >= 1 and num <= 5:
       dec =  True
    return dec

def charGender():
    gender = ""
    num = random.randint(1,7)
    if num >= 1 and num <= 3:
        gender = "Male"
    elif num >=4 and num <=6:
        gender = "Female"
    elif num == 7:
        gender = "Non-Binary"
    return gender
    
def getCharClass():
    charClass = ""
    classInt = random.randint(1,43)
    if classInt == 1:
        charClass = "Cleric"
    elif classInt == 2:
        charClass = "Wizard"
    elif classInt == 3:
        charClass = "Warlock" 
    elif classInt == 4:
        charClass = "Shaman" 
    elif classInt == 5:
        charClass = "Druid" 
    elif classInt == 6:
        charClass = "Ally" 
    elif classInt == 7:
        charClass = "Coward" 
    elif classInt == 8:
        charClass = "Egg" 
    elif classInt == 9:
        charClass = "Flagbearer" 
    elif classInt == 10:
        charClass = "Mercenary"
    elif classInt == 11:
        charClass = "Monger"
    elif classInt == 12:
        charClass = "Ninja"
    elif classInt == 13:
        charClass = "Pilot"
    elif classInt == 14:
        charClass = "Processor"
    elif classInt == 15:
        charClass = "Rebel"
    elif classInt == 16:
        charClass = "Samurai"
    elif classInt == 17:
        charClass = "Spellshaper"
    elif classInt == 18:
        charClass = "Citizen"
    elif classInt == 19:
        charClass = "Deserter"
    elif classInt == 20:
        charClass = "Scion"
    elif classInt == 21:
        charClass = "Serf"
    elif classInt == 22:
        charClass = "Survivor"
    elif classInt == 23:
        charClass = "Advisor"
    elif classInt == 24:
        charClass = "Archer"
    elif classInt == 25:
        charClass = "Artificer"
    elif classInt == 26:
        charClass = "Assassin"
    elif classInt == 27:
        charClass = "Barbarian"
    elif classInt == 28:
        charClass = "Berserker"
    elif classInt == 29:
        charClass = "Drone"
    elif classInt == 30:
        charClass = "Elder"
    elif classInt == 31:
        charClass = "Knight"
    elif classInt == 32:
        charClass = "Mystic"
    elif classInt == 33:
        charClass = "Noble"
    elif classInt == 34:
        charClass = "Nomad"
    elif classInt == 35:
        charClass = "Peasant"
    elif classInt == 36:
        charClass = "Pirate"
    elif classInt == 37:
        charClass = "Praetor"
    elif classInt == 38:
        charClass = "Rigger"
    elif classInt == 39:
        charClass = "Rogue"
    elif classInt == 40:
        charClass = "Scout"
    elif classInt == 41:
        charClass = "Soldier"
    elif classInt == 42:
        charClass = "Spawn"
    elif classInt == 43:
        charClass = "Warrior"
    return charClass

def getColors():
    color = ""
    colorInt = random.randint(1,122)
    if colorInt == 1:
        color = "White, Blue, Black, and Red"
    elif colorInt == 2:
        color = "Blue, Black, Red, and Green"
    elif colorInt == 3:
        color = "Black, Red, Green, and White"
    elif colorInt == 4:
        color = "Red, Green, White, and Blue"
    elif colorInt == 5:
        color = "Green, White, Blue, and Black"
    elif colorInt == 6 or colorInt == 7:
        color = "White, Blue, Black, Red, and Green"
    elif colorInt >= 8 and colorInt <= 10:
        color = "White, Blue, and Black"
    elif colorInt >= 11 and colorInt <= 13:
        color = "Blue, Black, and Red"
    elif colorInt >= 14 and colorInt <= 16:
        color = "Black, Red, and Green"
    elif colorInt >= 17 and colorInt <= 19:
        color = "Red, Green, and White"
    elif colorInt >= 20 and colorInt <= 22:
        color = "Green, White, and Blue"
    elif colorInt >= 23 and colorInt <= 25:
        color = "White, Black, and Red"
    elif colorInt >= 26 and colorInt <= 28:
        color = "Blue, Red, and Green"
    elif colorInt >= 29 and colorInt <= 31:
        color = "Black, White, and Green"
    elif colorInt >= 32 and colorInt <= 34:
        color = "Red, White, and Blue"
    elif colorInt >= 35 and colorInt <= 37:
        color = "Green, Blue, and Black"
    elif colorInt >= 38 and colorInt <= 42:
        color = "White and Blue"
    elif colorInt >= 43 and colorInt <= 47:
        color = "Blue and Black"
    elif colorInt >= 48 and colorInt <= 52:
        color = "Black and Red"
    elif colorInt >= 53 and colorInt <= 57:
        color = "Red and Green"
    elif colorInt >= 58 and colorInt <= 62:
        color = "Green and White"
    elif colorInt >= 63 and colorInt <= 67:
        color = "White and Black"
    elif colorInt >= 68 and colorInt <= 72:
        color = "Blue and Red"
    elif colorInt >= 73 and colorInt <= 77:
        color = "Black and Green"
    elif colorInt >= 78 and colorInt <= 82:
        color = "Red and White"
    elif colorInt >= 83 and colorInt <= 87:
        color = "Green and Blue"
    elif colorInt >= 88 and colorInt <= 94:
        color = "White"
    elif colorInt >= 95 and colorInt <= 101:
        color = "Blue"
    elif colorInt >= 102 and colorInt <= 108:
        color = "Black"
    elif colorInt >= 109 and colorInt <= 115:
        color = "Red"
    elif colorInt >= 116 and colorInt <= 122:
        color = "Green"
    return color

main()