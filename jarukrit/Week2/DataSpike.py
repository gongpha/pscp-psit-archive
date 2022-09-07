"""Prints something to console"""


def main() -> int:
    """The main function"""
    higest = None
    first = int(input())
    second = int(input())
    if first > second:
        higest = first
    else:
        higest = second
    third = int(input())
    if third > higest:
        higest = third
    fo_rth = int(input())
    if fo_rth > higest:
        higest = fo_rth
    fifth = int(input())
    if fifth > higest:
        higest = fifth
    sixth = int(input())
    if sixth > higest:
        higest = sixth
    seventh = int(input())
    if seventh > higest:
        higest = seventh
    eigth = int(input())
    if eigth > higest:
        higest = eigth
    print(higest)
    return 0

if __name__ == "__main__":
    main()
