from player import Player
from dealer import Dealer

class Blackjack(object):
	"""docstring for Blackjack"""

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

	def __str__(self):
		return '''=======blackjack game=======
how to play:
-
-
-
-
'''


	def run(self):

		blackjack = Blackjack()
		print(blackjack)

		player = Player()
		dealer = Dealer()

		print(player.show_hand())
		print(player.is_empty_hand())
		blackjack.hit(player, dealer)
		print(player.show_hand())
		print(player.is_empty_hand())


if __name__ == '__main__':
    Blackjack().run()