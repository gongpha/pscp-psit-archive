""" _ """

def main():
    """ _ """
    tttmap = [input() for _ in range(3)]
    winner = ''
    for iii in range(3):
        if tttmap[iii][0] == tttmap[iii][1] == tttmap[iii][2] != "-":
            winner = tttmap[iii][0]
            break
        if tttmap[0][iii] == tttmap[1][iii] == tttmap[2][iii] != "-":
            winner = tttmap[0][iii]
            break
    if tttmap[0][0] == tttmap[1][1] == tttmap[2][2] != "-":
        winner = tttmap[0][0]
    elif tttmap[0][2] == tttmap[1][1] == tttmap[2][0] != "-":
        winner = tttmap[0][2]

    print("DRAW" if winner == '' else '%s WIN' % winner)

main()
