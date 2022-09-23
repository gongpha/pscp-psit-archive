""" _ """
def main():
    """ _ """
    length = int(input())
    align = input()
    text = input()

    if align == "left":
        print(text.ljust(length))
    elif align == "right":
        print(text.rjust(length, " "))
    else:
        aligned = text.center(length, " ")
        if len(text) % 2 != 0 and length % 2 == 0:
            aligned = ' ' + aligned
            aligned = aligned[:-1]
        print(aligned)

main()
