from random import shuffle
import card

class Deck:

	def __init__(self):
		# creating a list of card obejcts
		self.all_cards = []

		for suit in card.suits:
			for rank in card.ranks:
				# create a card object
				created_card = card.Card(suit,rank)
				self.all_cards.append(created_card)

		# shuffle the deck of cards
	def shuffle_deck(self):
		shuffle(self.all_cards)

	def get_card(self):
		return self.all_cards.pop()

# new_deck = Deck()

# bottom_card = new_deck.all_cards[-1]
# print(bottom_card,'\n')

# new_deck.shuffle_deck()
# for card_object in new_deck.all_cards:
# 	print(card_object)
# print('\n')

# mycard = new_deck.get_card()
# print(mycard)

# print(len(new_deck.all_cards))