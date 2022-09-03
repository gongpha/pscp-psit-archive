"""Prints something to console"""


def main() -> int:
    """The main function"""
    choice = int(input())
    if choice == 1:
        print("In Deep Learning, a Convolutional Neural Network (CNN) is"
              " a class of Deep Neural Networks, most commonly applied"
              " to analyzing visual imagery.")
    elif choice == 2:
        print('\"Two things are infinite: the universe and human stupidity;'
              ' and I\'m not sure about the universe\". - Albert Einstein')
    elif choice == 3:
        print('Statistics is the discipline that concerns the collection,'
              ' organization, displaying, analysis, interpretation'
              ' and presentation of data.')
    elif choice == 4:
        print('The backslash (\\) is a typographical mark used mainly in'
              ' computing and is the mirror image of the common slash (/).'
              ' It is sometimes called \"escape character\".')
    return 0


if __name__ == "__main__":
    main()
