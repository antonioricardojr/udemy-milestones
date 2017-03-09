class Player(object):
	
	"""class for a player"""

	def __init__(self, bankroll=100):
		super(Player, self).__init__()
		self.bankroll = bankroll

	def add_bankroll(sel, amount):
		self.bankroll += amount

		
class Card(object):
	
	"""A class for the cards"""
	def __init__(self, name, value, suit):
		self.name = name
		self.value = value
		self.suit = suit


class Deck(object):
	
	"""A class to represent a Deck"""
	def __init__(self, cards, ace_as_ten = False):
		
		self.ace_as_ten = ace_as_ten
		self.cards = generate_deck()
		self.removed_cards = []

	def generate_deck():

		suits = ["hearts", "spades","diamonds" "clubs"]
		cards = []

		for suit in suits:
			if self.ace_as_ten:
				ace = Card("Ace", 10, suit)
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

	def remove_from_top():
		self.removed_cards.append(self.cards.pop())

	def remove_card(self, card):
		for c in self.cards:
			if card.name == c.name and card.suit == c.suit:
				self.cards.remove(c):
				self.removed_cards.append(c)


