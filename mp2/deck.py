from card import Card
from random import shuffle

class Deck(object):
	
	"""A class to represent a Deck of cards"""
	def __init__(self, ace_as_eleven = False):
		
		self.ace_as_eleven = ace_as_eleven
		self.cards = self.generate_deck()
		self.removed_cards = []

	def generate_deck(self):
		"""It generates a deck of 52 cards"""
		suits = ["hearts", "spades","diamonds","clubs"]
		cards = []

		for suit in suits:
			if self.ace_as_eleven:
				ace = Card("Ace", 11, suit)
			else:
				ace = Card("Ace", 1, suit)
			cards.append(ace)

			two = Card("Two", 2, suit)
			cards.append(two)
			
			three = Card("Three", 3, suit)
			cards.append(three)

			four = Card("Four", 4, suit)
			cards.append(four)

			five = Card("Five", 5, suit)
			cards.append(five)

			six = Card("Six", 6, suit)
			cards.append(six)

			seven = Card("Seven", 7, suit)
			cards.append(seven)

			eight = Card("Eight", 8, suit)
			cards.append(eight)

			nine = Card("Nine", 9, suit)
			cards.append(nine)

			ten = Card("Ten", 10, suit)
			cards.append(ten)

			jack = Card("Jack", 10, suit)
			cards.append(jack)

			queen = Card("Queen", 10, suit)
			cards.append(queen)

			king = Card("King", 10, suit)
			cards.append(king)

		return cards

	def get_from_top(self):
		'''It gets one card from the top of the deck'''
		try:
			card = self.cards.pop()
			self.removed_cards.append(card)
			return card
		except:
			print("There is no cards!")

	def remove_card(self, card):
		'''It removes one specific card from the deck'''
		for c in self.cards:
			if card.name == c.name and card.suit == c.suit:
				self.cards.remove(c)
				self.removed_cards.append(c)
				return c

	def shuffle():
		return shuffle(self.cards)
