from .card import Card, Deck, card_from_str, hand_from_str


def test_card():
    card = Card(0)
    # this will be Ad (ace of diamonds)
    assert "A♢" == str(card)


def test_adding_cards_adds_values():
    a = Card(0)  # Ad
    b = Card(10) # Jd
    assert 11 == a + b 


def test_draw():
    for n in range(1, 12):
        deck = Deck()
        cards = list(deck.draw(n))
        assert n == len(cards)


def test_card_from_str():
    s = "Ks"  # ace of diamonds
    card = card_from_str(s)
    assert "Ks" == card.ascii_str


def test_hand_from_str():
    s = "Ad Ac Ah As 10s"
    values = [1, 1, 1, 1, 10]
    hand, turn_card = hand_from_str(s)
    cards = hand + [turn_card]
    for expect, card in zip(values, cards):
        assert expect == card.value
