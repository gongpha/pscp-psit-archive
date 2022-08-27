""" _ """

def main():
    """ _ """
    xxx = int(input())
    yyy = int(input())

    if xxx == 0 and yyy == 0:
        print("O")
    else:
        if xxx == 0:
            print("Y")
        elif yyy == 0:
            print("X")
        elif xxx < 0:
            if yyy < 0:
                print("Q3")
            else:
                print("Q2")
        else:
            if yyy < 0:
                print("Q4")
            else:
                print("Q1")

main()
