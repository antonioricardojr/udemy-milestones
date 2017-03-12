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

	def is_empty_hand(self):
		return len(self.hand) == 0

	def show_hand(self):
		print("---player's hand---")
		for card in self.hand:
			print(card)
		print("total points: {points}".format(points = self.hand_points()))
		print("bet: {bet}".format(bet = self.bet))
		print("bankroll: {bankroll}".format(bankroll = self.bankroll))

	def hand_points(self):
		resp = 0
		for card in self.hand:
			resp += card.value

		return resp
					
