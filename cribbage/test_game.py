from nose.tools import assert_equal

from .game import game, Hand, Game 
from .players import RandomPlayer


def test_deal():
	dealer = RandomPlayer()
	pone = RandomPlayer()
	hand = Hand(dealer, pone)

	hand.deal() 

	cases = [
		(6, dealer), 
		(6, pone),
	]
	for expected, player in cases:
		yield assert_equal, expected, len(player.hand) 


def test_discards():
	dealer = RandomPlayer()
	pone = RandomPlayer()
	hand = Hand(dealer, pone)

	hand.deal() 
	hand.discards() 

	cases = [
		(4, dealer), 
		(4, pone),
	]
	for expected, player in cases:
		yield assert_equal, expected, len(player.hand) 

def test_turn_card():
	


def test_count_hands():
	dealer = RandomPlayer()
	pone = RandomPlayer()
	hand = Hand(dealer, pone)

	hand.deal() 
	hand.discards() 
	hand.count_hands()

	cases = [
		(4, dealer), 
		(4, pone),
	]
	for expected, player in cases:
		yield assert_equal, expected, len(player.hand) 

	cases = [
		(4, dealer), 
		(0, pone),
	]
	for expected, player in cases:
		yield assert_equal, expected, len(player.crib) 


# def test_single_hand():
# 	dealer = RandomPlayer()
# 	pone = RandomPlayer()
# 	hand = Hand(dealer, pone)

# 	hand.deal() 
# 	hand.discards() 
# 	hand.counting() 
# 	hand.count_hands()

# 	cases = [
# 		(4, dealer), 
# 		(4, pone),
# 	]
# 	for expected, player in cases:
# 		yield assert_equal, expected, len(player.hand) 

# 	cases = [
# 		(4, dealer), 
# 		(0, pone),
# 	]
# 	for expected, player in cases:
# 		yield assert_equal, expected, len(player.crib) 
