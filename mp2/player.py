class Player(object):
	
	"""class for a player"""

	def __init__(self, bankroll=100, hand=[], bet=0):
		super(Player, self).__init__()
		self.bankroll = bankroll
		self.hand = hand
		self.bet = bet

	def add_bankroll(sel, amount):
		self.bankroll += amount

	def make_bet(self,value):
		if self.bankroll >= value:
			self.bankroll -= value
			self.bet += value
		else:
			print("You don't have enough money!")
		
	def draw_a_card(self, card):
		self.hand.append(card)
