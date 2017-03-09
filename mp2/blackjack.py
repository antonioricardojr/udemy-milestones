class Blackjack(object):
	"""docstring for Blackjack"""
	def __init__(self):

	def hit(self, player, dealer):
		card = dealer.give_a_card()
		player.draw_a_card(card)


	def double(self, player):
		player.make_bet(2*self.player.bet)
		self.hit(player)


	def split(self, player):
		pass

	def surrender(self, player):
		pass
		