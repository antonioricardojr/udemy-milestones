from player import Player
from dealer import Dealer

class Blackjack(object):
	"""docstring for Blackjack"""

	def __init__(self):
		self.has_winner = False

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

	def choose_option(self):
		print('''
1 - hit
2 - double
3 - split
4 - surrender
		''')
		option = input("option?")
		return option



	def run(self):

		blackjack = Blackjack()
		print(blackjack)

		player = Player()
		dealer = Dealer()

		while not self.has_winner:
			option = self.choose_option()
			if option == 1:
				self.hit(player, dealer)
			elif option == 2:
				self.double(player)
			elif option == 3:
				pass
			else:
				exit()

			print(player.show_hand())
			print(player.is_empty_hand())

if __name__ == '__main__':
    Blackjack().run()