# Python program to play a two card draw game against the computer. Best hand: Pair of Aces.
import random

# Generate the list of cards based on the information below.
cardlist = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "Ace": 14, }
suits = {"Spades", "Clubs", "Diamonds", "Hearts"}
color = {"Black", "Red"}
cards = []
for cardname in cardlist:
    for suit in suits:
        cards.append(
            {"Value": cardlist[cardname], "Card": cardname, "Suit": suit})

# Random select two cards for the user.
usercards = random.sample(cards, 2)
usersum = sum([c['Value'] for c in usercards])

# Random select two cards for the computer
pccards = random.sample(cards, 2)
pcsum = sum([c['Value'] for c in pccards])

#Win condition, lose condition, overall logic.
if usersum > pcsum:
    print("You win")
    print("Your Cards: " + str(usercards))
    print("PC Cards: " + str(pccards))
elif pcsum > usersum:
    print("You lost!")
    print("PC Cards: " + str(pccards))
    print("Your Cards: " + str(usercards))
elif pcsum == usersum:
    print("You tied!")
    print("PC Cards: " + str(pccards))
    print("Your Cards: " + str(usercards))
