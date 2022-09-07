'''Test'''
def main():
    '''Also test'''
    cards = []
    score, ace = 0, 0
    for _ in range(int(input())):
        cards.append(input())
    for card in cards:
        card = card.upper()
        if card.isnumeric():
            score += int(card)
        elif card == "J" or card == "K" or card == "Q":
            score += 10
        elif card == "A":
            score += 11
            ace += 1
    while score > 21 and ace > 0:
        score -= 10
        ace -= 1
    print(score)
main()
