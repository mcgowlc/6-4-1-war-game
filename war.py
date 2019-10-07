import random
import card.py
import deck.property
import hand.property
import player.py
import table.py
import stack.py


def main():
    table = Table(['Matthew', 'Mark', 'Luke', 'John'])
    table.deal_cards()
    table.play_all()

def print_underline(string, line):
    print('\n{}\n{}'.format(string, line * len(string)))
