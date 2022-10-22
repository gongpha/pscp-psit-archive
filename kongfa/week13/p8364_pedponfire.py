""" _ """
def main():
    """ _ """
    ducks = [int(input()) for i in range(int(input()))]
    abst = int(input())
    exacthalf = ducks.count(abst / 2)
    print(
        ((exacthalf * (exacthalf - 1) // 2) if exacthalf > 1 else 0) +
        sum(
            ducks.count(i) * ducks.count(abst - i)
            for i in sorted(set(sorted(ducks)))
            if i < abst / 2
        )
    )
main()
