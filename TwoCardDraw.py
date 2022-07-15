import random

cardlist = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "Ace": 11,}
suits = {"Spades", "Clubs", "Diamonds", "Hearts"}
color = {"Black", "Red"}
cards = []
for cardname in cardlist:
    for suit in suits:
        cards.append({"Value": cardlist[cardname], "Card": cardname, "Suit": suit})

pccardnames = random.sample(cards, 2)
pcsum = sum([c['Value'] for c in pccardnames])

usercardnames = random.sample(cards, 2)
usersum = sum([c['Value'] for c in usercardnames])

if usersum > pcsum:
    print("You win")
    print("Your Cards: " + str(usercardnames))
    print("PC Cards: " + str(pccardnames))
elif pcsum > usersum:
    print("You lost!")
    print("PC Cards: " + str(pccardnames))
    print("Your Cards: " + str(usercardnames))
elif pcsum == usersum:
    print("You tied!")
