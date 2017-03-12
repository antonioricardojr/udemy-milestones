import random
from deck import *
from player import Player
		
class Dealer(Player):
	"""docstring for Dealer"""
	def __init__(self):
		Player.__init__(self, hand = [])
		self.deck = Deck()	

	def get_deck(self):
		return self.deck

	def set_deck(self, new_deck):
		self.deck = new_deck

	def deck_shuffle(self):
		self.deck.set_cards(random.sample(self.deck.get_cards(), len(self.deck.get_cards())))

	def give_a_card(self):
		return self.deck.get_from_top()