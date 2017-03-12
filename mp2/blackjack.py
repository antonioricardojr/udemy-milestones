from player import Player
from dealer import Dealer

class Blackjack(object):

	def hit(self, player, dealer):
		card = dealer.give_a_card()
		player.draw_a_card(card)

	def double(self, player, dealer):
		player.make_double()
		self.hit(player, dealer)

	def has_winner(self, player, dealer):
		if player.hand_points() < 21 and dealer.hand_points() < 21:
			return False
		elif player.hand_points() == 21: # the player won
			return True
		elif dealer.hand_points() == 21: # the dealer wins.
			return True
		elif player.hand_points() > 21: # the player lose.
			print("The player lose")
			return True
		elif dealer.hand_points() > 21: # the player wins.
			return True
		else:
			return False

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
		dealer.deck_shuffle()
		player.make_bet(10)

		while not self.has_winner(player, dealer):
			option = self.choose_option()
			if option == 1:
				self.hit(player, dealer)
			elif option == 2:
				self.double(player, dealer)
			elif option == 3:
				pass
			else:
				exit()

			print(player.show_hand())
			print(player.is_empty_hand())

if __name__ == '__main__':
    Blackjack().run()