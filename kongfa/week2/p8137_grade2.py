""" _ """

def main():
    """ _ """
    point = int(float(input()))

    if point > 100 or point < 0:
        print("ERR")
        return

    print(
        "A" if point >= 95 else
        "B+" if point >= 90 else
        "B" if point >= 85 else
        "C+" if point >= 80 else
        "C" if point >= 75 else
        "D+" if point >= 70 else
        "D" if point >= 65 else
        "F+" if point >= 60 else
        "F"
    )

main()
