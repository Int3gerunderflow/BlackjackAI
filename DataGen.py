#File to create data needed for the ML algorithms
#Conventional card counting techniques are simulated with a 2 card deck

#Code for the game itself
import random

# Define the card values and suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

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

# Main game function
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_hand(player_hand, 'Player')
    display_hand(dealer_hand[:1], 'Dealer')

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to [h]it or [s]tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand, 'Player')
        else:
            break

    while calculate_hand_value(dealer_hand) < 18:
        dealer_hand.append(deck.pop())

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

if __name__ == "__main__":
    play_blackjack()