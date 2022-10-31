import random
deck = 1

card_pool = [1,1,1,1,13,13,13,13,12,12,12,12,11,11,11,11,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]

def card_makeup():
    global card_pool
    ace = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    jack = 0
    queen = 0
    king = 0
    joke = 0
    for i in enumerate(card_pool):
        if i[1] == 1:
            ace += 1
        elif i[1] == 2:
            two += 1
        elif i[1] == 3:
            three += 1
        elif i[1] == 4:
            four += 1
        elif i[1] == 5:
            five += 1
        elif i[1] == 6:
            six += 1
        elif i[1] == 7:
            seven += 1
        elif i[1] == 8:
            eight += 1
        elif i[1] == 9:
            nine += 1
        elif i[1] == 10:
            ten += 1
        elif i[1] == 11:
            jack += 1
        elif i[1] == 12:
            queen += 1
        elif i[1] == 13:
            king += 1
        elif i[1] == 14:
            joke += 1
    print("In this deck there are...\n", str(ace), "Aces\n", str(two), "Twos\n", str(three), "Threes\n", str(four),"Fours\n", str(five), "Fives\n",str(six),"Sixes\n",str(seven),"Sevens\n", str(eight),"Eights\n",str(nine),"Nines\n",str(ten),"Tens\n",str(jack),"Jacks\n", str(queen),"Queens\n",str(king),"Kings\n And...", str(joke), "Jokers!!")


def from_deck():
    pool = -1
    global card_pool
    global deck
    for i in enumerate(card_pool):
        pool += 1
    if pool == 0:
        pool = -1
        shuffle_deck()
        for i in enumerate(card_pool):
            pool += 1
    card_choice = random.randrange(0, pool)
    card = card_pool[card_choice]
    remove_card = card_pool[card_choice]
    card_pool.remove(remove_card)
    return card

def shuffle_deck():
    global card_pool
    global deck
    deck += 1
    deck_version = random.randint(1,5)
    if deck_version == 1:
        card_pool = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,5,6,7,14,8,5,6,7,8,5,6,7,8,5,6,7,8,9,10,11,12,13,9,10,11,12,13,9,10,11,12,13,9,10,11,12,13]
        print("You got Deck 1")
    elif deck_version == 2:
        card_pool = [13,11,9,6,7,5,4,12,1,3,2,8,10,13,11,9,6,7,5,4,12,1,3,2,8,10,13,11,9,6,7,5,4,14,12,1,3,2,8,10,13,11,9,6,7,5,4,12,1,3,2,8,10]
        print("You got Deck 2")
    elif deck_version == 3:
        card_pool = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,14,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
        print("You got Deck 3")
    elif deck_version == 4:
        card_pool = [13,12,13,12,13,12,13,12,11,10,11,10,11,10,11,10,9,8,9,14,8,9,8,9,8,7,6,7,6,7,6,7,6,5,4,5,4,5,4,5,4,3,2,3,2,3,2,3,2,1,1,1,1]
        print("You got Deck 4")
    elif deck_version == 5:
        card_pool = [1,1,13,14,12,13,12,13,12,13,14,12,11,10,11,10,11,10,11,10,14,9,8,9,8,9,8,9,14,8,7,6,7,6,7,14,6,7,6,5,4,5,4,5,4,5,4,14,3,2,3,2,3,2,3,2,1,1,14,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,1,1,13,11,9,6,7,5,4,12,1,3,2,8,10,13,11,9,6,7,5,4,12,1,3,2,8,10,13,11,9,6,7,5,4,12,1,3,2,8,10,13,11,9,6,7,5,4,12,1,3,2,8,10,1,13,13,13,13,12,12,12,12,11,11,11,11,10,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,5,6,7,8,5,6,7,8,5,6,7,8,5,6,7,8,9,10,11,12,13,9,10,11,12,13,9,10,11,12,13,9,10,11,12,13,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]
        print("You got Deck 5    :)")
    return deck_version

def card_sorting_hand(card, hand):
    hand = hand
    if card > 1 and card <= 10:
        hand += card
    elif card == 1:
        hand += 1
    elif card == 11:
        hand += 10
    elif card == 12:
        hand += 10
    elif card == 13:
        hand += 10
    elif card == 14:
        hand = 200
    return hand

def card_sorting_ctype(card):
    global ctype
    if card > 1 and card <= 10:
        ctype = str(card)
    elif card == 1:
        ctype = "ACE"
    elif card == 11:
        ctype = "JACK"
    elif card == 12:
        ctype = "QUEEN"
    elif card == 13:
        ctype = "KING"
    elif card == 14:
        ctype = "JOKER"
    return ctype