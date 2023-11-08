cards = {
         'S2': 2,
         'S3': 3,
         'S4': 4,
         'S5': 5,
         'S6': 6,
         'S7': 7,
         'S8': 8,
         'S9': 9,
         'S10': 10,
         'SJ': 11,
         'SQ': 12,
         'SK': 13,
         'SA': 14
}

def check_straight(card1: str, card2: str, card3: str):
    cardvals = [cards[card1], cards[card2], cards[card3]]
    sorttime = sorted(cardvals)
    lowest = min(sorttime)
    highest = max(sorttime)
    cardvalues = set(range(lowest, highest+1))
    if set(sorttime) == cardvalues:
        return highest
    else:
        return 0



def check_3ofa_kind(card1: str, card2: str, card3: str):
    if card1 == card2 == card3:
        return cards[card1]
    else:
        return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    leftcards = [left1, left2, left3]
    rightcards = [right1, right2, right3]

    if check_straight(left1, left2, left3) and check_straight(right1, right2, right3):
        if max(leftcards) > max(rightcards):
            return -1
        elif max(leftcards) < max(rightcards):
            return 1
        else:
            return 0

    if check_3ofa_kind(left1, left2, left3) and check_3ofa_kind(right1, right2, right3):
        if leftcards[0] > rightcards[0]:
            return -1
        elif leftcards[0] < rightcards[0]:
            return 1
        else:
            return 0

    if check_royal_flush(left1, left2, left3) and not check_royal_flush(right1, right2, right3):
        return -1
    if check_royal_flush(right1, right2, right3) and not check_royal_flush(left1, left2, left3):
        return 1

    if check_straight(left1, left2, left3) and check_3ofa_kind(right1, right2, right3):
        return -1
    if check_straight(right1, right2, right3) and check_3ofa_kind(left1, left2, left3):
        return 1

    return 0

