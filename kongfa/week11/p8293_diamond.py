""" _ """


def main():
    """ _ """
    mmm = int(input())
    nnn = int(input())
    diamonds = [
        input().split()
        for _ in range(mmm)
    ]
    print(max([
        sum([
            int(j[i])
            for j in diamonds
        ])
        for i in range(nnn)
    ]))


main()
