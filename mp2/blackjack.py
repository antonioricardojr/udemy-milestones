from player import Player
from dealer import Dealer

class Blackjack(object):

	def give_hands(self, dealer, player):

		card = dealer.give_a_card()
		player.draw_card(card)
		card = dealer.give_a_card()
		player.draw_card(card)

		card = dealer.give_a_card()
		dealer.draw_card(card)
		card = dealer.give_a_card()
		dealer.draw_card(card)
		
	
	def has_winner(self, dealer, player):
		if player.hand_points() < 21 and dealer.hand_points() < 21:
			return False
		elif player.hand_points() == 21 or dealer.hand_points() == 21:
			return True
		elif player.hand_points() > 21 or dealer.hand_points() > 21:
			return True
		else:
			return False		

	def choose_option(self):
		print('''
		1 - hit
		2 - surrender
		''')
		opt = raw_input('option? ')

		return opt

	def give_card(self, dealer, player):
		card = dealer.give_a_card()
		player.draw_card(card)

	def run(self):

		player = Player()
		dealer = Dealer()

		dealer.deck_shuffle()

		self.give_hands(dealer, player)

		player.show_hand()
		dealer.show_hand()

		while not self.has_winner(dealer, player):
			opt = self.choose_option()

			if opt == "1":
				self.give_card(dealer, player)
			else:
				quit()


			player.show_hand()
			dealer.show_hand()
			

if __name__ == '__main__':
    Blackjack().run()