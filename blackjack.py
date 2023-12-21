import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_still_going = True

def check_for_blackjack(dealer_hand, user_hand):
    if sum(dealer_hand) == 21:
        print("The dealer got Blackjack, the dealer wins.")
        
    elif sum(user_hand) == 21:
        print("You got Blackjack, you win!")
        
    elif sum(dealer_hand) == 21 and sum(user_hand) == 21:
        print("You both got Blackjack, dealer wins. ")
        

while game_still_going:
    dealer_hand = random.sample(cards,3)
    user_hand = random.sample(cards,3)
    dealer_score = 0
    user_score = 0
    dealer_score += sum(dealer_hand)
    user_score += sum(user_hand)

    if user_score > 21:
        for i in range(len(user_hand)):
            if user_hand[i] == 11:
                user_hand[i] = 1
                user_score += sum(user_hand)

            
        print("went over 21")
    
    check_for_blackjack(dealer_hand, user_hand)
    print(f"initial user hand: {user_hand}")
    

    print(f"""
        Dealer Hand: {dealer_hand}  Dealer Score: {dealer_score}
        Player Hand: {user_hand}    Player Score: {user_score}
""")
    
        
    break
    