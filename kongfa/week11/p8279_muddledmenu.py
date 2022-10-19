""" _ """


def main():
    """ _ """
    menu = []
    while True:
        inv = input()
        if inv == "DONE":
            break
        elif inv == "CLOSED":
            menu = []
            break
        elif inv == "SOMETHING'S WRONG":
            menu = []
        else:
            if inv.startswith("Can't do: "):
                if inv[10:] in menu:
                    menu.remove(inv[10:])
                continue
            inv = inv.split(" #")
            if inv[1] == "N":
                menu.append(inv[0])
            else:
                menu.insert(int(inv[1]) - 1, inv[0])
    print("Full Course: %s Reversed: %s" % (
        menu, menu[::-1]
    ))


main()
