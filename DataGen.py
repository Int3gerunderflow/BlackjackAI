#File to create data needed for the ML algorithms
#Conventional card counting techniques are simulated with a 2 card deck

#Code for the game itself
import random

# Define the card values and suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

#global variable to keep track of the count
card_count = 0
ace_count = 0

# Function to create and shuffle the deck
def create_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append((value, suit))
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    ace_count = 0

    for card in hand:
        #a card is a tuple of 2 items: value and suit
        value += card_values[card[0]]
        if card[0] == 'Ace':
            ace_count += 1

    #in blackjack if it prevents the player from going bust aces count as 1
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1

    return value

# Function to display the hand
def display_hand(hand, name):
    print(f"{name}'s hand:")
    for card in hand:
        print(f"  {card[0]} of {card[1]}")
    print(f"Total value: {calculate_hand_value(hand)}\n")


#card counting mechanism
#cards will be counting per the Omega II system
def count_cards(new_cards):
    global card_count
    for card in new_cards:
        match card_values[card[0]]:
            case 2: 
                card_count += 1
            case 3: 
                card_count += 1
            case 7: 
                card_count += 1
            case 4: 
                card_count += 2
            case 5: 
                card_count += 2
            case 6: 
                card_count += 2  
            case 8: 
                card_count += 0
            case 9: 
                card_count -= 1 
            case 10: 
                card_count -= 2
            case 11: 
                card_count -= 2
            case _:
                continue


# Main game function
def hit_or_stand(hand, dealer):
    print(dealer[0][0] + "njganjadfadgoj")

    if (calculate_hand_value(hand) <= 17 and ace_count != 0): return "h"
    elif(ace_count != 0 and calculate_hand_value(hand) == 18):
        if (int(dealer[0][0]) < 9): return "s"
        else: return "h"
    elif (calculate_hand_value(hand) <= 11): return "h"
    elif (calculate_hand_value(hand) ==12):
        if (int(dealer[0][0]) ==4 or int(dealer[0][0]) == 5 or int(dealer[0][0]) ==6): return "s"
        else: return "h"
    elif (calculate_hand_value(hand) >= 13 and calculate_hand_value(hand) <=16):
        if (dealer[0][0] != "Ace" and int(dealer[0][0]) <= 6): return "s"
        else: return "h"
    else: "s"



def play_blackjack():
    deck = create_deck()
    
    wantToPlay = True
    while wantToPlay:
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        display_hand(player_hand, 'Player')
        display_hand(dealer_hand[:1], 'Dealer')

        #each time any new cards are shown make note of them in the count
        count_cards(player_hand + dealer_hand[:1])

        while calculate_hand_value(player_hand) < 21:
            #decide whther to hit or stand
            action = hit_or_stand(player_hand, dealer_hand)

            #action = input("Do you want to [h]it or [s]tand? ").lower()
            if action == 'h':
                new_card = deck.pop()
                count_cards([new_card])
                player_hand.append(new_card)
                display_hand(player_hand, 'Player')
            else:
                break

        #compensate for the fact that first card is hidden
        count_cards([dealer_hand[1]])
        while calculate_hand_value(dealer_hand) < 18:
            new_card = deck.pop()
            count_cards([new_card])
            dealer_hand.append(new_card)

        display_hand(dealer_hand, 'Dealer')

        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        if player_value > 21:
            print("Player busts! Dealer wins.")
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        playAgain = input("Do you want to play again (y/n)? ").lower()

        if playAgain != 'y':
            wantToPlay = False

if __name__ == "__main__":
    play_blackjack()