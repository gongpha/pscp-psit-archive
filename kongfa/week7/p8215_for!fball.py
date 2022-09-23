""" _ """
def main():
    """ !!! USE 0 1 2 as ball locations !!! """
    ball = 0
    sequence = input()
    for ccc in sequence:
        if ccc == 'A':
            if ball == 0:
                ball = 1
            elif ball == 1:
                ball = 0
        elif ccc == 'B':
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        elif ccc == 'C':
            if ball == 0:
                ball = 2
            elif ball == 2:
                ball = 0
    print(ball + 1)
main()
