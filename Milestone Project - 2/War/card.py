# CARD
# SUIT,RANK,VALUE

suits = ('Hearts','Diamonds','Spade','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:

	def __init__(self,suit,rank):
		self.suit = suit.capitalize()
		self.rank = rank.capitalize()
		self.value = values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit

# two_of_spade = Card('Spade','Two')
# print(two_of_spade.rank)
# print(two_of_spade)

# king_of_clubs = Card('Clubs','King')
# print(king_of_clubs.suit)
# print(king_of_clubs)

# print(two_of_spade.value > king_of_clubs.value)

