""" _ """
def main():
    """ _ """
    prize1 = input()
    prizel2 = input()
    prizef3p1 = input()
    prizef3p2 = input()
    prizel3p1 = input()
    prizel3p2 = input()
    lotto = input()

    prize = 0

    if lotto == prize1:
        prize += 6000000
    if prize1 == '999999':
        if lotto == '000000' or lotto == '999998':
            prize += 100000
    elif prize1 == '000000':
        if lotto == '999999' or lotto == '000001':
            prize += 100000
    elif abs(int(lotto) - int(prize1)) == 1:
        prize += 100000

    if lotto[4:] == prizel2:
        prize += 2000
    if lotto[:3] == prizef3p1:
        prize += 4000
    if lotto[:3] == prizef3p2:
        prize += 4000
    if lotto[3:] == prizel3p1:
        prize += 4000
    if lotto[3:] == prizel3p2:
        prize += 4000
    print(prize)

main()
