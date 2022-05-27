import cardclass
import deckclass
import handclass
import chipsclass

playing = True

def take_bet(chips):    # here chips is Chips class object

	while True:
		try:
			chips.bet = int(input('How many chips would you like to bet? '))
		except:
			print('Sorry please provide an integer value')
		else:
			if chips.bet > chips.total:
				print('Sorry, you do not have enough chips! You have : {} chips'.format(chips.total))
			else:
				break

def hit(deck,hand):      # here deck and hand are Deck and Hand class objects respectively.

	hand.add_card(deck.deal())
	hand.adjust_ace_value()

def hit_or_stand(deck,hand):
	global playing    # to control an upcoming while loop

	while  True:
		x = input('Hit or Stand? Enter h or s ')

		if x[0].lower() == 'h':       # .lower in case player enter HIT, hh, stand, etc
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player Stands, Dealer's Turn.")
			playing = False
			break

		else:
			print("Sorry, I did not understand that, Please enter h or s only!")
			continue

def show_some(player,dealer):   # here player and dealer are Hand class function

	# show only ONE of the dealer's cards
	print("\nDealer's Hand: ")
	print('First card hidden!')
	print(dealer.cards[1])      # showing the second card of the dealer

	# show all (2 cards) of the player's hand/cards
	print("\nPlayer's Hand: ")
	for card in player.cards:
		print(card)

def show_all(player,dealer):

	# show all of the dealer's cards
	print("\nDealer's Hand: ")
	for card in dealer.cards:
		print(card)

	# the above thing can also be done as:
	#print("\n Dealer's Hand: ",*dealer.cards, sep='\n')

	print(f"Value of Dealer's hand is: {dealer.value}")    # printing dealer's cards value

	# show all of the player's hand/cards
	print("\nPlayer's Hand: ")
	for card in player.cards:
		print(card)

	print(f"Value of Player's hand is: {player.value}")    # printing dealer's cards value

# End of the game scenario

def player_busts(player,dealer,chips):
	print("BUST PLAYER!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("BUST DEALER!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("DEALER WINS!")
	chips.lose_bet()

def push(player,dealer):
	print("Dealer and Player tie! PUSH")


# GAME LOGIC

player_chips = None   # for keeping player chips in check if player plays another game

while True:
	# Priting opening statement
	print("WELCOME TO BLACKJACK")

	# Create and Shuffle the deck, deal two cards to each player
	deck = deckclass.Deck()
	deck.shuffle_deck()

	player_hand = handclass.Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = handclass.Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Set up the Player's chips
	if player_chips == None:
		player_chips = chipsclass.Chips()

	# Prompt the player for their bet
	take_bet(player_chips)

	# show cards (but one dealer card remains hidden)
	show_some(player_hand,dealer_hand)

	while playing:
		
		# prompt for Player to Hit or Stand
		hit_or_stand(deck,player_hand)

		# If the player's hand exceeds 21, run player_busts() and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

		# show cards (but one dealer card remains hidden)
		show_some(player_hand,dealer_hand)

	# If player's hasn't busted, play Dealer's hand until dealer reaches 17
	if player_hand.value <= 21:

		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		# show all cards
		show_all(player_hand,dealer_hand)

		# Run different winning scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	# Inform Player about their chips total
	print("\nPlayer's total chips are at: {}".format(player_chips.total))
	# Ask to play again
	new_game = input("Would you like to play another hand? (y/n) : ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print('Thank you for playing!')
		break