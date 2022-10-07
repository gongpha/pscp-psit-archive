""" _ """
def main():
    """ _ """
    seq = input()
    tup = tuple(seq.split(' '))
    wha = input()
    con = tup.count(wha)
    idx = str(tup.index(wha))
    print("\n".join([
        " ".join([
            idx
            for _ in range(con)
        ])
        for _ in range(con)
    ]))
main()
