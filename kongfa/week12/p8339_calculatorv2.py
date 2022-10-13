""" _ """
def main():
    """ _ """
    xxx = int(input())
    print(
        1 if xxx == 1 else
        int(str(len(str(xxx)) - 1) + ('8' * (len(str(xxx)) - 1)) + '9') + (
            ((xxx - int('1' + len(str(xxx)) * '0')) + 1) * len(str(xxx))
        ) + xxx
    )
main()
