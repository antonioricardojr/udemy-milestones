class Card(object):
	
	def __init__(self, name, value, suit):
		self.name = name
		self.value = value
		self.suit = suit

	def get_name(self):
		return self.name

	def get_value(self):
		return self.value

	def get_suit(self):
		return self.suit

	def __str__(self):
		return '{name} of {suit}'.format(name = self.name, suit = self.suit)