import card
import deck
import player

# get a new deck
new_deck = deck.Deck()

# shuffle the deck
new_deck.shuffle_deck()

# creating two players
player1 = player.Player('One')
player2 = player.Player('Two')

# distribute cards to the players by equally splitting the deck in two
for x in range(26):
	player1.add_cards(new_deck.get_card())
	player2.add_cards(new_deck.get_card())

round_num = 0
game_on = True

while game_on:

	round_num += 1
	print(f'Round {round_num}')

	if len(player1.all_cards) == 0:
		print('Player One, out of cards! Player Two Wins!')
		game_on = False
		break

	if len(player2.all_cards) == 0:
		print('Player Two, out of cards! Player One Wins!')
		game_on = False
		break

	# START A NEW ROUND
	player1_cards = []
	player1_cards.append(player1.remove_card())
	
	player2_cards = []
	player2_cards.append(player2.remove_card())
	
	at_war = True

	while at_war:
		if player1_cards[-1].value > player2_cards[-1].value:
			print('Player One takes the round!')
			player1.add_cards(player1_cards)
			player1.add_cards(player2_cards)
			at_war = False

		elif player1_cards[-1].value < player2_cards[-1].value:
			print('Player Two takes the round')
			player2.add_cards(player1_cards)
			player2.add_cards(player2_cards)
			at_war = False
		
		else:
			print('WAR!')

			# if any player does not have alteast 5 cards at war he looses
			if len(player1.all_cards) < 5:
				print('Player One unable to declare war')
				print('Player Two WINS!')
				game_on = False
				break

			elif len(player2.all_cards) < 5:
				print('Player Two unable to declare war')
				print('Player One WINS!')
				game_on = False
				break

			else:
				for num in range(3):
					player1_cards.append(player1.remove_card())
					player2_cards.append(player2.remove_card())