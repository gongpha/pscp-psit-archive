""" _ """

def main():
    """ _ """
    hour = int(input())
    minute = int(input())

    hand_delta = 1 / 60
    hand_short = ((hour * 60) + minute) / 720
    hand_long = minute / 60
    hand_angle = hand_short - hand_long
    print(
        abs(hand_angle) < hand_delta and
        hand_angle >= 0
    )


main()
