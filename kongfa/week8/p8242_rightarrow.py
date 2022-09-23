""" _ """
def main():
    """ _ """
    count = int(input())
    line = int(input())
    space = int(line * 0.5)
    go_pos = False
    space_current = 0
    for _ in range(line):
        print(" " * space_current, "*" * count, sep="")
        if space_current >= space:
            go_pos = True
        space_current += -1 if go_pos else 1
main()
