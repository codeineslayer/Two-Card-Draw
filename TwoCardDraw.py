# Python program to play a two card draw game against the computer. Best hand: Pair of Aces.
import random
from colorama import init, Fore, Style
init(convert=True)

SUIT_SIZE = 13
DRAW_AMOUNT = 2
SUITS = {
        "spades": {
          "display": Fore.BLACK + "♠" + Style.RESET_ALL,
            },
        "clubs": {
            "display": Fore.BLACK + "♣" + Style.RESET_ALL
            },
        "diamonds": {
            "display": Fore.RED + "♦" + Style.RESET_ALL
            },
        "hearts": {
            "display": Fore.RED + "♥" + Style.RESET_ALL
            }
        }
DECK = []

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def value(self):
        if self.number == 1:
            value = 14
        else:
            value = self.number
        return int(value)

    def print_format(self):
        output = ""
        if self.number == 11:  # Jack
            output = "J"
        elif self.number == 12:  # Queen
            output = "Q"
        elif self.number == 13:  # King
            output = "K"
        elif self.number == 1:  # Ace
            output = "A"
        else:
            output = str(self.number)
        return output

    def print_to_screen(self):
        return "%s%s" % (self.print_format(), SUITS[self.suit]['display'])

    def __repr__(self):
        return "%s-%s-%s" % (self.print_format(), self.suit, self.value())


def populate_deck():
    for suit in SUITS.keys():
        for n in range(1, SUIT_SIZE+1):
            card = Card(n, suit)
            DECK.append(card)


if __name__ == "__main__":
    usercards = []
    pccards = []

    # Populate the DECK
    populate_deck()
    # shuffle DECK
    random.shuffle(DECK)

    for i in range(1, DRAW_AMOUNT+1):
        usercards.append(DECK.pop())
        pccards.append(DECK.pop())

    usersum = sum([x.value() for x in usercards])
    pcsum = sum([x.value() for x in pccards])

    if usersum > pcsum:
        outcome = "win"
    elif usersum < pcsum:
        outcome = "lose"
    else:
        outcome = "tie"

    print("You %s!" % outcome)
    print("Your hand: %s" % (' '.join([x.print_to_screen() for x in usercards])))
    print("PC's hand: %s" %  (' '.join([x.print_to_screen() for x in pccards])))