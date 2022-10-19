""" _ """


def main():
    """ _ """
    found = []
    while True:
        inv = input()
        if inv == "END":
            break
        elif inv == "IT'S A DOG":
            found.pop()
        else:
            found += inv.split(", ")
    print("\n".join([
        "%s %d %s" % (each, found.index(each) + 1, found.count(each))
        for each in sorted(set(found))
    ]))


main()
