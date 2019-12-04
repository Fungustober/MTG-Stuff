#Ben B
#---------------------------
#The purpose of this program is to have an easy way to create a deck.
#---------------------------
def main():
    wType = getType()
    deckFile = checkWtype(wType)
    
    cat = "deck"+str(deckFile)+".dek"
    
    if wType == 1:
        #print('Hi1')
        deck = open(cat, 'w')
        editDeck(wType, deck)
        print("The cards were written to the deck file.")
        deck.close()
    elif wType == 2:
        eDeck(cat)
        print("The deck was edited.")
    elif wType == 3:
        #print('Hi3')
        deck = open(cat, 'w')
        deck.close()
        print("Deck deleted")
        #for count in range(0,3):
        #decklist = [["",""]]*
    #deck.close()
    ans = input("Would you like to create/destroy/edit another deck? (y/n) ")
    while ans == 'y' or ans == 'Y':
        wType = getType()
        deckFile = checkWtype(wType)
    
        cat = "deck"+str(deckFile)+".dek"
    
        if wType == 1:
            deck = open(cat, 'w')
            editDeck(wType, deck)
            print("The cards were written to the deck file.")
            deck.close()
        elif wType == 2:
            eDeck(cat)
            print("The deck was edited.")
        elif wType == 3:
            deck = open(cat, 'w')
            deck.close()
            print("Deck deleted")
        ans = input("Would you like to create/destroy/edit a deck? (y/n) ")

def getType():
    print("Enter a number for what you would like to do.")
    print("1 = New Deck; 2 = Edit a deck; 3 = Delete deck")
    wType = int(input("Enter a number: "))
    while wType > 3 or wType < 1:
        wType = int(input("ERROR: Number must be 1, 2, or 3! Re-enter a number: "))
    return wType

def checkWtype(wType):
    if wType == 1:
        for count in range(0,100):
            cat = "deck"+str(count)+".dek"
            
            deck = open(cat, 'a')
            deck.close()
            
            deck = open(cat, 'r')
            
            line1 = deck.readline()
            line1M = line1.rstrip('\n')
            
            if line1M != '|':
                deck.close()
                return count
            elif line1M == '|':
                deck.close()
    elif wType == 2 or wType ==3:
        fileNum = int(input("Enter the file number(goes from 0 to 99): "))
        while fileNum > 99 or wType < 0:
            fileNum = int(input("ERROR: Number must be between 0 and 99! Re-enter a number: "))
        return fileNum

def editDeck(wType, deck):
    if wType == 1:
        deck.write('|\n')
        name = input("Give the deck a name: ")
        deck.write(name+"\n")
        print("Enter a format. (The list is Vintage, Legacy, Modern, Pauper, Pioneer, Standard, Brawl, Commander, Historic)")
        dFormat = input("What format is the deck? ")
        deck.write("Format: \n")
        deck.write(dFormat+"\n")
        if dFormat == "Commander":
            comm = input("Please enter your commander: ")
            cardCount = 99
            deck.write("Cards in deck: \n"+str(cardCount+1)+"\nMainboard: \n\nCommander: ")
            deck.write(comm+"\n"+"\n")
            addCards(cardCount, deck, dFormat)
            return
        elif dFormat == "Brawl":
            comm = input("Please enter your commander: ")
            cardCount = 59
            deck.write("Cards in deck: \n"+str(cardCount+1)+"\nMainboard: \n\nCommander: \n"+comm+"\n"+"\n")
            addCards(cardCount, deck, dFormat)
            return
        else:
            cardCount = int(input("Enter the amount of cards in your deck (min 60): "))
            while cardCount < 60:
                cardCount = int(input("The amount of cards in your deck must be greater than or equal to 60! Re-enter a number: "))
            deck.write("Cards in deck: \n"+str(cardCount)+"\nMainboard: \n\n")
            addCards(cardCount, deck, dFormat)
            return

def addCards(cardCount, deck, dFormat):
    while cardCount > 0:
        card = input("Enter a card in the deck: ")
        num = int(input("How many of those cards are in the deck? "))
        deck.write(card+"\n"+str(num)+"\n")
        cardCount -= num
    deck.write("\nSideboard: \n\n")
    ans = input("Would you like to add cards to the sideboard? (y/n) ")
    if ans == 'y' or ans == "Y":
        cardCount = 15
        while cardCount > 0:
            card = input("Enter a card, or enter nul to quit: ")
            if card == "nul":
                return
            num = int(input("How many of those cards are in the sideboard? "))
            deck.write(card+"\n"+str(num)+"\n")
            cardCount -= num
    return

def eDeck(cat):
    decklist = []
    deck = open(cat, 'r')
    deck.readline()
    name = deck.readline()
    name1 = name.rstrip('\n')
    deck.readline()
    deFormat = deck.readline()
    deFormat1 = deFormat.rstrip('\n')
    deck.readline()
    cC = deck.readline()
    cC1 = cC.rstrip('\n')
    cardCount = int(cC1)
    deck.readline()
    if deFormat1 == 'Brawl' or deFormat1 == 'Commander':
        deck.readline()
        deck.readline()
        command = deck.readline()
    deck.readline()
    card = deck.readline()
    card = card.rstrip('\n')
    while card != '':
        if card != '':
            decklist.append(card)
            num = deck.readline()
            num = num.rstrip('\n')
            decklist.append(num)
            card = deck.readline()
            card = card.rstrip('\n')
            #print("hi")
    deck.readline()
    card = deck.readline()
    card = card.rstrip('\n')
    sideboard = []
    while card != '':
        if card != '':
            sideboard.append(card)
            num = deck.readline()
            num = num.rstrip('\n')
            sideboard.append(num)
            card = deck.readline()
            card = card.rstrip('\n')
    
    deck.close()
    ans = ''
    while ans != "none" and ans != "None" and ans != "NONE":
        print()
        print("Name: "+name1)
        print("Format: "+deFormat1)
        print("Number of cards: "+str(cardCount))
        print("Mainboard: ")
        if deFormat1 == "Brawl" or deFormat1 == "Commander":
            print("Commander: "+ command)
        print()
        for index in range(0, len(decklist)):
            print("["+str(index)+"]\t"+decklist[index])
        print("To change an element, input 'name', 'format', '#' (number of cards), 'address' (editing a card or number of a card), or 'none'") 
        ans = input("Which element would you like to edit? ")
        if ans == "name" or ans == "Name" or ans == "NAME":
            #print("hi1")
            name1 = input("What would you like to rename the deck? ")
            print("Deck has been renamed.")
        elif ans == "format" or ans == "Format" or ans == "FORMAT":
            #print("hi2")
            deFormat1 = input("What format would you like for this deck instead? (if you need to add cards, edit the .dek file with a text editor) ")
            print("Format has been changed.")
        elif ans == "#":
            #print("hi3")
            cardCount = int(input("How many cards would you like the deck to have? (if you need to add cards, edit the .dek file with a text editor) "))
            print("Number of cards in deck has been changed.")
        elif ans == "address" or ans == "Address" or ans == "ADDRESS":
            #print('hi4')
            ind = int(input("Which address would you like to edit? (one of the numbers in brackets) "))
            decklist[ind] = input("What value would you like the address to contain? ")
            print("Value of address has been changed.")
        elif ans == "add" or ans == "Add" or ans == "ADD":
            cA = input("What card would you like to add? ")
            nU = input("How many of those cards would be in the deck? ")
            deck.append(cA)
            deck.append(nU)
        elif ans == "remove" or ans == "Remove" or ans == "REMOVE":
            ind = int(input("Which card would you like to remove? (type the card's address, which is the number in brackets next to a card) "))
            while ind % 2 != 0:
                ind = int(input("ERROR: address must refer to a card."))
            decklist[ind] = ''
            decklist[ind+1] = ''
        elif ans == "none" or ans == "None" or ans == "NONE":
            print('')
        else:
            print("Command not found.")
    
    print('')
    print("Sideboard: ")
    ens = ''
    while ens != 'n' and ens != 'no' and ens != 'No' and ens != 'NO': 
        for index in range(0, len(sideboard)):
            print("["+str(index)+"]\t"+sideboard[index])
        ens = input("Would you like to edit the sideboard? ")
        if ens != 'n' and ens != 'no' and ens != 'No' and ens != 'NO':
            print("To change an element, input 'address' (changes specific things), 'add', or 'remove'")
            ans = input("What would you like to edit? ")
            if ans == 'address' or ans == 'Address' or ans == 'ADDRESS':
                ind = int(input("Which address would you like to edit? (one of the numbers in brackets) "))
                sideboard[ind] = input("What value would you like the address to contain? ")
                print("Value of address has been changed.")
            elif ans == 'add' or ans == 'Add' or ans == 'ADD':
                cA = input("What card would you like to add? ")
                nU = input("How many of those cards would be in the sideboard? ")
                deck.append(cA)
                deck.append(nU)
            elif ans == 'remove' or ans == 'Remove' or ans == 'REMOVE':
                ind = int(input("Which card would you like to remove? (type the card's address, which is the number in brackets next to a card) "))
                while ind % 2 != 0:
                    ind = int(input("ERROR: address must refer to a card."))
                decklist[ind] = ''
                decklist[ind+1] = ''
            else:
                print('Command not found')
    
    print('')
    print("Writing to file...")
    
    deck = open(cat, 'w')
    deck.write('|\n')
    deck.write(name1+'\n')
    deck.write("Format: \n")
    deck.write(deFormat1+'\n')
    deck.write("Cards in deck: \n"+str(cardCount)+"\nMainboard: \n\n")
    if deFormat1 == 'Brawl' or deFormat1 == 'Commander':
        deck.write('Commander: \n')
        deck.write(command+'\n')
    
    for index in range(0, len(decklist)):
        deck.write(str(decklist[index])+'\n')
    
    deck.write('\n')
    deck.write('Sideboard: \n\n')
    
    for index in range(0, len(sideboard)):
        deck.write(str(sideboard[index])+'\n')

main()