""" _ """
def main():
    """ _ """
    yyy = int(input())
    print(
        "Yes" if (
            yyy % 400 == 0 and yyy % 100 == 0
        ) or (
            yyy % 4 == 0 and yyy % 100 != 0
        ) else "No")
main()
