import random
from art import logo
import os

def clear():
    os.system("clear")

def check_for_blackjack(user_hand, dealer_hand):
    if sum(dealer_hand) == 21:
        return False
    elif sum(user_hand) == 21:
        return True

def ace_value(hand):
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

def print_hands_scores():
    print(f"Your final hand: {user_hand}  Final score: {user_score}")
    print(f"Dealers final hand: {dealer_hand}  Final score: {dealer_score}\n")

def who_won(user_score, dealer_score):
    if dealer_score > 21:
        print("You win, the dealer busted!\n")
    elif user_score > 21:
        print("You busted. You lose.\n")
    elif user_score > dealer_score:
            print("You Win! :)\n")
    elif dealer_score > user_score:
            print("Sorry you lose. :( \n")
    else:
        print("Its a Draw!\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_still_going = True        
while game_still_going:
    play_again = input("Would you like to play Blackjack? Type 'y' for yes or 'n' for no: ")
    if play_again == 'y':
        clear()
        print(logo)

        dealer_hand = random.sample(cards, 2)  
        user_hand = random.sample(cards, 2)
        dealer_score = sum(dealer_hand)
        user_score = sum(user_hand)        
        
        print(f"Your cards: {user_hand}, Current Score: {user_score}\n")  
        print(f"Dealers first card: {dealer_hand[0]}\n")
        if check_for_blackjack(user_hand, dealer_hand) == True:
            print("You got blackjack, you win!\n")
            continue
        else:
            if check_for_blackjack(user_hand, dealer_hand) == False:
                print(f"Dealers Hand: {dealer_hand}\n")
                print("The Dealer got Blackjack, the Dealer wins.\n")
                continue
        
        hit_me = True
        while hit_me:
            another_card = input("Type 'y' to get another card, type 'p' to pass: " ).lower()
            print()
            clear()
            print(logo)
            if another_card == 'y':
                user_hand += random.sample(cards, 1)
                ace_value(user_hand)
                user_score = sum(user_hand)
                if user_score > 21:
                    print(f"Your cards: {user_hand}, Current Score: {user_score}\n")
                    print("Ouch you Busted. Game Over.\n")
                    break
                else:
                    print(f"Your cards: {user_hand}, Current Score: {user_score}\n")
                    print(f"Dealers first card: {dealer_hand[0]}\n")
                    continue
            else:
                hit_me = False
                clear()
                print(logo)
                print("You chose to pass.\n")
                while dealer_score < 17:
                    dealer_hand += random.sample(cards, 1)
                    ace_value(dealer_hand)
                    dealer_score = 0
                    dealer_score += sum(dealer_hand)
                print_hands_scores()
                who_won(user_score, dealer_score)       
    else:
        game_still_going = False
        print("Goodbye. ")



        



            
        
    
    
    
    


    
        

    