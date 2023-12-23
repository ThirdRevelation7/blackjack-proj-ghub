import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_still_going = True

def check_for_blackjack(user_hand, dealer_hand):
    if sum(user_hand) == 21 and sum(dealer_hand) == 21:
        return False
    elif sum(user_hand) == 21:
        return True
    elif sum(dealer_hand) == 21:
        return False

def ace_value(hand):
    for i in range(len(hand)):
        if hand[i] == 11:
            hand[i] = 1
           
while game_still_going:
    print(logo)
    dealer_hand = []
    while sum(dealer_hand) < 16:
        dealer_hand += random.sample(cards, 1)  
    user_hand = random.sample(cards, 2)
    dealer_score = 0
    user_score = 0
    dealer_score += sum(dealer_hand)
    user_score += sum(user_hand)
    
    print(f"Your cards: {user_hand}, Current Score: {user_score}")  
    print(f"Dealers first card: {dealer_hand[0]}")
    if check_for_blackjack(user_hand, dealer_hand) == True:
        print("You got blackjack, you win!")
        game_still_going = False
    elif check_for_blackjack(user_hand, dealer_hand) == False:
        print(f"Dealers Hand: {dealer_hand}")
        print("The Dealer got Blackjack, the Dealer wins. Sorry.")
        game_still_going = False
    else:
        another_card = input("Type 'y' to get another card, type 'p' to pass: ").lower()
        if another_card == 'y':
            user_hand += random.sample(cards, 1)
            new_score = sum(user_hand)
            if sum(user_hand) > 21:
                ace_value(user_hand)
                print(f"Your cards: {user_hand}, Current Score: {sum(user_hand)}")
            else:
                print(f"Your cards: {user_hand}, Current Score: {sum(user_hand)}")
            
        elif another_card == 'p' and dealer_score < 16:
            dealer_hand += random.sample(cards, 1)

        
        print(dealer_hand)


            
        
    
    
    
    


    
        
    break
    