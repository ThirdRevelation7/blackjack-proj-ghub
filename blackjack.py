import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_still_going = True

def clear():
    os.system("clear")

def check_for_blackjack(user_hand, dealer_hand):
    if sum(user_hand) == 21 and sum(dealer_hand) == 21:
        return False
    elif sum(user_hand) == 21:
        return True
    elif sum(dealer_hand) == 21:
        return False

def ace_value(hand):
    if sum(hand) > 21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1

def who_won(user_score, dealer_score):
    if dealer_score > 21:
        print(f"Your final hand: {user_hand}  Final score: {user_score}")
        print(f"Dealers final hand: {dealer_hand}  Final score: {dealer_score}\n")
        print("You win, the dealer busted!\n")
        
    else:
        if user_score > dealer_score:
            print(f"Your final hand: {user_hand}  Final score: {user_score}")
            print(f"Dealers final hand: {dealer_hand}  Final score: {dealer_score}\n")
            print()
            print("You Win! :)\n")
            
        elif dealer_score > user_score:
            print(f"Your final hand: {user_hand}  Final score: {user_score}")
            print(f"Dealers final hand: {dealer_hand}  Final score: {dealer_score}\n")
            print()
            print("Sorry you lose. :( \n")
            
        else:
            print(f"Your final hand: {user_hand}  Final score: {user_score}")
            print(f"Dealers final hand: {dealer_hand}  Final score: {dealer_score}\n")
            print()
            print("Its a Draw!\n")
           
while game_still_going:
    play_again = input("Would you like to play Blackjack? Type 'y' for yes or 'n' for no: ")
    if play_again == 'y':
        clear()
        print(logo)

        dealer_hand = random.sample(cards, 2)  
        user_hand = random.sample(cards, 2)
        dealer_score = 0
        user_score = 0
        dealer_score += sum(dealer_hand)
        user_score += sum(user_hand)        
        
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
                print("You passed.")
                while dealer_score < 16:
                    dealer_hand += random.sample(cards, 1)
                    ace_value(dealer_hand)
                    dealer_score = 0
                    dealer_score += sum(dealer_hand)
                who_won(user_score, dealer_score)       
    else:
        game_still_going = False
        print("Goodbye. ")



        



            
        
    
    
    
    


    
        

    