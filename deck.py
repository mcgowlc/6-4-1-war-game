class Deck:

    def __init__(self):
        self.cards = [Card(s, r) for s in Card.SUITE for r in Card.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def setup_hands(self, players):
        hands = [player.hand for player in players]
        while len(self.cards) >= len(players):
            for hand in hands:
                hand.add_card(self.cards.pop())
        return hands
