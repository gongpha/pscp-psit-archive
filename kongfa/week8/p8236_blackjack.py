""" recy ? """

TABLE_TEN = ["J", "Q", "K", "10"]

def main():
    """ _ """
    count = int(input())
    cards = []
    for _ in range(count):
        cards.append(input())
    total = 0
    ace_found = False
    for ccc in cards:
        if ccc == 'A':
            total += 1
            ace_found = True
        elif ccc in TABLE_TEN:
            total += 10
        else:
            total += int(ccc)
    if ace_found and total < 12:
        total += 10
    print(total)
main()
