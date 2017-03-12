import random
from deck import *


class Dealer(object):
	"""docstring for Dealer"""
	def __init__(self ):
		super(Dealer, self).__init__()
		self.deck = Deck()
		self.hand = []

	def deck_shuffle(self):
		self.deck.cards = random.sample(self.deck.cards, len(self.deck.cards))

	def two_cards(self,is_for_dealer=False):
		resp = []

		if not is_for_dealer:
			resp.append(self.deck.get_from_top())
			resp.append(self.deck.get_from_top())
		else:
			self.hand.append(self.deck.get_from_top())
			self.hand.append(self.deck.get_from_top())

		return resp

	def give_a_card(self):
		return self.deck.get_from_top()

	def hand_points(self):
		resp = 0
		for card in self.hand:
			resp += card.value
		return resp
		