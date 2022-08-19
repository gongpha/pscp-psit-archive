""" _ """
def main():
    """ _ """
    count = int(input())
    line = int(input())
    space = int(line * 0.5)
    go_pos = False
    for _ in range(line):
        print(" " * space, "*" * count, sep="")
        if space <= 0:
            go_pos = True
        space += 1 if go_pos else -1
main()
