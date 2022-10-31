import card_physics
import time

#Varible for tracking games
pl_wins = 0
de_wins = 0
ties = 0
round = 1
decisions = 0
card = 0
hand = 0
ctype = "Card"
dcard = 0
dhand =0

#For while loops
looped = True
deciding = True
allow = False
con = True
#Full Game

#For first deck

while looped:
    if round == 1:
        print("Fresh Deck!")
    if card_physics.deck == 2:
        if con:
            print("The Joker has been added! :)")
            con = False
    else:
        print("Currently on deck #" + str(card_physics.deck))

    if hand == 0:
        time.sleep(1)
        print()
        print("START GAME #" + str(round))
        print()
    game = True
    while game:
        deciding = True
        card = card_physics.from_deck()
        hand = card_physics.card_sorting_hand(card, hand)
        ctype = card_physics.card_sorting_ctype(card)
        deciding = True
        time.sleep(1)
        #This if-else statement ends the game for 21 and over, resets to looped loop
        if hand == 200:
            print("Your card is a JOKER!!!\nYOU WIN!!!!!")
            game = False
            hand = 0
            pl_wins += 1
            round += 1
            break
        elif ctype == "ACE":
            choice = int(input("You got an ACE! Will it be a 1 or an 11? (Enter 1 or 11) "))
            if choice == 1:
                continue
            elif choice == 11:
                hand += 10
            else:
                print("Guess it's a 1.")
            decisions += 1
            print("Your hand is:", str(hand))
        elif hand == 21:
            print("Your card is a", ctype + "!\nYour hand is:", str(hand))
            print()
            print("BLACKJACK! You win!")
            game = False
            hand = 0
            pl_wins += 1
            round += 1
            break
        elif hand > 21:
            print("Your card is a", ctype + "!\nYour hand is:", str(hand))
            print()
            print("You exceeded 21! You lose.")
            game = False
            hand = 0
            de_wins += 1
            round += 1
            break
        #Beginning of deciding loop, which is where player decisions are made
        else:
            print("Your card is a", ctype + "!\nYour hand is:", str(hand))
            print()
        if dhand == 0:
            dcard = card_physics.from_deck()
            dhand = card_physics.card_sorting_hand(dcard, dhand)
            ctype = card_physics.card_sorting_ctype(dcard)
            time.sleep(1)
            if dhand != 200:
                print("Dealer's card is a", ctype + "!\nTheir hand is", str(dhand))
                print()
            else:
                print("The Dealer got the JOKER!!!\nYou Lose the round!!!!")
                deciding = False
                game = False
                de_wins += 1
                hand = 0
                dhand = 0
                round += 1
        while deciding:
            decisions += 1
            time.sleep(1)
            print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
            if round >= 10 or decisions >= 15:
                print("5. Shuffle Deck")
                allow = True
            print()
            decision = int(input("Choose an option: "))
            print()
            #Ends deciding loop and goes to game loop
            if decision == 1:
                deciding = False
                break
            #Decides game ending and goes back to looped loop
            elif decision == 2:
                while dhand <= 16:
                    dcard = card_physics.from_deck()
                    dhand = card_physics.card_sorting_hand(dcard, dhand)
                    ctype = card_physics.card_sorting_ctype(card)

                    if dhand > 21:
                        print("Dealer's hand:", str(dhand))
                        print("Your hand is:", str(hand))
                        print()
                        print("You win!")
                        print()
                        pl_wins += 1
                        deciding = False
                        game = False
                        hand = 0
                        dhand = 0
                        round += 1
                        break

                    elif dhand > hand and dhand > 16:
                        print("Dealer's hand:", str(dhand))
                        print("Your hand is:", str(hand))
                        print()
                        print("Dealer wins!")
                        print()
                        de_wins += 1
                        deciding = False
                        game = False
                        hand = 0
                        dhand = 0
                        round += 1
                        break

                    elif dhand < hand and dhand > 16:
                        print("Dealer's hand:", str(dhand))
                        print("Your hand is:", str(hand))
                        print()
                        print("You win!")
                        print()
                        pl_wins += 1
                        deciding = False
                        game = False
                        hand = 0
                        dhand = 0
                        round += 1
                        break

                    elif dhand == hand and dhand > 16:
                        print("Dealer's hand:", str(dhand))
                        print("Your hand is:", str(hand))
                        print()
                        print("It's a tie! No one wins!")
                        print()
                        ties += 1
                        deciding = False
                        game = False
                        hand = 0
                        dhand = 0
                        round += 1
                        break

            #Gives stats, then loops deciding
            elif decision == 3 and round != 1:
                print("Currently on Deck #" + str(card_physics.deck) + ".")
                time.sleep(0.25)
                print("Current on Round #" + str(round) + ".")
                time.sleep(0.25)
                print("You have made " + str(decisions), "decisions.")
                time.sleep(0.25)
                print("Number of Player wins:", str(pl_wins))
                time.sleep(0.25)
                print("Number of Dealer wins:", str(de_wins))
                time.sleep(0.25)
                print("Number of tie games:", str(ties))
                time.sleep(0.25)
                print("Total # of games played is:", str(round - 1))
                time.sleep(0.25)
                print("Percentage of Player wins:", str(f'{(pl_wins / (round - 1) * 100):.1f}' + "%"))
                time.sleep(0.25)
                card_physics.card_makeup()
                print()
                continue

            #Kills all loops ending the game instantly
            elif decision == 4:
                looped = False
                game = False
                deciding = False
                hand = "Done"
                dhand = "Done"
                round += 1
                break
            elif decision == 5 and allow:
                card_physics.shuffle_deck()
                print("You are now on deck #", str(card_physics.deck))
            else:
                time.sleep(0.5)
                if round == 1 and decision == 3:
                    print("Not enough rounds!")
                    time.sleep(0.25)
                    print("Please enter an integer value of 1, 2, or 4.")
                    print()
                elif not allow:
                    print("Invalid input!")
                    time.sleep(0.25)
                    print("Please enter an integer value between 1 and 4.")
                    print()
                else:
                    print("Invalid input!")
                    time.sleep(0.25)
                    print("Please enter an integer value between 1 and 5.")
                    print()
                time.sleep(0.5)