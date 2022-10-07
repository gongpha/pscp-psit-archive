""" _ """


def main():
    """ _ """
    distance = int(input())
    print((sorted([input().split() + [i] for i, _ in enumerate(range(int(input())))],
                  key=lambda x: ((distance - float(x[1])) / float(x[0]), x[1]))[0])[2] + 1)


main()
