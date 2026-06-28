from random import sample

SUITS = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
NUMBERS = ['2', 'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3']


def create_deck():
    """建立一副牌"""
    return [(suit, number) for suit in SUITS for number in NUMBERS]


def deal_cards(deck):
    """隨機發兩張牌給兩位玩家"""
    return sample(deck, k=2)


def get_card_value(card):
    """取得牌的大小分數"""
    suit, number = card

    number_score = len(NUMBERS) - NUMBERS.index(number)
    suit_score = len(SUITS) - SUITS.index(suit)

    return number_score, suit_score


def compare_cards(player1, player2):
    """比較兩張牌大小"""
    p1_value = get_card_value(player1)
    p2_value = get_card_value(player2)

    if p1_value > p2_value:
        return "player1 wins"
    elif p1_value < p2_value:
        return "player2 wins"
    else:
        return "draw"


def main():
    deck = create_deck()

    player1, player2 = deal_cards(deck)

    print(f"player1 {player1}, player2 {player2}")

    result = compare_cards(player1, player2)

    print(result)


main()