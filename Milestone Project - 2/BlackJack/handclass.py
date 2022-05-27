import cardclass
import deckclass

class Hand:

	def __init__(self):
		self.cards = []  # start with an empty list as we did in the Deck class
		self.value = 0   # start with zero value
		self.aces = 0    # add an attribute to keep track of aces

	def add_card(self,card):
		self.cards.append(card)     # here car d is Card class object
		self.value +=  cardclass.values[card.rank]

    	# track aces
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_ace_value(self):

    	# If total value > 21 and I still an ace
    	# than change my ace to be a 1 instead of an 11
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

# test_deck = deckclass.Deck()
# test_deck.shuffle_deck()

# # PLAYER
# test_player = Hand()
# # Deal 1 card from the deck CARD(suit,rank)
# pulled_card = test_deck.deal()
# print(pulled_card)

# test_player.add_card(pulled_card)
# print(test_player.value)