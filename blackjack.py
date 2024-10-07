import random

# ASCII art for card suits
SUITS = {
    'Hearts':    'H',
    'Diamonds':  'D',
    'Clubs':     'C',
    'Spades':    'S'
}

# Card values
VALUES = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10
}

def create_deck():
    # TODO: Create and return a list of tuples representing cards
    deck = []
    for value in VALUES:
        for suit in SUITS:
            deck.append((value, suit))
    return deck

def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_hand_value(hand):
    number_of_aces = 0
    hand_value = 0

    for card in hand:
        if card[0] == 'Ace':
            number_of_aces+=1
        hand_value+= VALUES[card[0]]
    
    while hand_value > 21 and number_of_aces > 0:
        hand_value -= 10
        number_of_aces -= 1

    return hand_value



def display_card(card):
    return f'{card[0]} of {card[1]}'


def display_hand(hand, hide_first=False):
    if hide_first:
        return f'[XXX], {display_card(hand[1])}'
    return ", ".join([display_card(card) for card in hand])

def play_blackjack():
    # Create the deck
    deck = create_deck()
    
    # Shuffle, and deal initial hands to player and dealer
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # TODO: Implement the main game loop
    # 1. Player's turn: hit or stand
    player_value = calculate_hand_value(player_hand)

    '''We'll implement a while loop to allow the player to hit or stand.'''
    # ======================================================================

    # while player_value < 21:



    if player_value > 21:
        print('\nPlayer Busted! Dealer wins.\n')
        return

    # ======================================================================

    # 2. Dealer's turn (if player hasn't busted)
    # Nothing to do here until step 3.
    if player_value <= 21:
        print('\nPlayer Turn Has Ended.\n')
        # Reveal dealer's hidden card
        print('Dealer hand:')
        print(display_hand(dealer_hand))

        # Calculate the value of the dealer's hand
        dealer_value = calculate_hand_value(dealer_hand)

        # Dealer hits until hand value is 17 or higher
        while dealer_value < 17:
            dealer_hand.append(deal_card(deck))
            dealer_value = calculate_hand_value(dealer_hand)

        # Display dealer's final hand
        print('Dealer hand:')
        print(display_hand(dealer_hand))
        
        
        # 3. Determine winner and display results
        # Check if dealer has busted

        # Compare player's and dealer's hand values


    # Game over
    print('Game over.')

if __name__ == "__main__":
    play_blackjack()