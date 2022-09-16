""" _ """
def main():
    """ _ """
    rra = int(input())
    rrb = int(input())

    print(
        "%.2f" % (1 / (1 + 10 ** ((rrb - rra) / 400))) if input() == 'A' else
        "%.2f" % (1 / (1 + 10 ** ((rra - rrb) / 400)))
    )

main()
