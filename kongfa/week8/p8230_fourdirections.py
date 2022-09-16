""" _ """
def main():
    """ _ """
    arrows = input()
    print('\n'.join([
        ' '.join([
            "  *  " if y == 1 or y == 5 else (
                " *   " * (x == 'L') + " *** " * (x == 'U') +
                "  *  " * (x == 'D') + "   * " * (x == 'R')
            ) if y == 2 else (
                "*****" * (x == 'L' or x == 'R') + "* * *" *
                (x == 'U' or x == 'D')
            ) if y == 3 else (
                " *   " * (x == 'L') + "  *  " * (x == 'U') +
                " *** " * (x == 'D') + "   * " * (x == 'R')
            )
            for x in arrows
        ])
        for y in range(1, 6)
    ]))
main()
