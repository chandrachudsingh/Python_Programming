from random import shuffle
import cardclass

class Deck:

	def __init__(self):
		# creating a list of card obejcts
		self.deck = []

		for suit in cardclass.suits:
			for rank in cardclass.ranks:
				# create a card object
				created_card = cardclass.Card(suit,rank)
				self.deck.append(created_card)

		# shuffle the deck of cards
	def shuffle_deck(self):
		shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += ' \n' + card.cardclass.__str__()

		return 'The deck has: ' + deck_comp

# new_deck = Deck()

# bottom_card = new_deck.card_deck[-1]
# print(bottom_card,'\n')

# new_deck.shuffle_deck()
# for card_object in new_deck.card_deck:
# 	print(card_object)
# print('\n')

# mycard = new_deck.deal()
# print(mycard)

# print(len(new_deck.card_deck))