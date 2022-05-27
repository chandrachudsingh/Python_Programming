class Chips:

	def __init__(self,total=100):
		self.total = total        # can be set to default value or supplied by the user
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet