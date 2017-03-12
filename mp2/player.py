class Player(object):

	def __init__(self, hand=[]):
		self.hand = hand

	def get_hand(self):
		return self.hand
		
	def draw_card(self, card):

		self.hand.append(card)

	def is_empty_hand(self):
		return len(self.hand) == 0

	def show_hand(self):
		print("---{player}'s hand---").format(player = "Player")
		for card in self.hand:
			print(card)
		print("total points: {points}".format(points = self.hand_points()))

	def hand_points(self):
		resp = 0
		for card in self.hand:
			resp += card.value

		return resp