import deck

class Player:

	def __init__(self,name):
		self.name = name
		self.all_cards = []

	def remove_card(self):
		return self.all_cards.pop(0)    # to remove a card from the top of the deck/list

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):         # if there are a list of cards
			self.all_cards.extend(new_cards)    # to add list of cards in case of 'war' situation
		else:
			self.all_cards.append(new_cards)    # add a single card to the deck

	def __str__(self):
		return f'PLayer {self.name} has {len(self.all_cards)} cards.'

# new_player = Player('Chandra')
# print(new_player)

# new_deck2 = deck.Deck()
# my_card = new_deck2.get_card()

# new_player.add_cards(my_card)
# print(new_player)

# new_player.add_cards([my_card,my_card,my_card])
# print(new_player)

# new_player.remove_card()
# print(new_player)