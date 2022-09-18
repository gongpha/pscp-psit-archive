""" _ """
def main():
    """ _ """
    number = input()
    print(
        "+66" + number[1:-8]
        if input() == "International" else
        number[:-8], number[-8:-4], number[-4:]
    )
main()
