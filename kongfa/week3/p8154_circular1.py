""" _ """
def main():
    """ _ """
    xxx1 = float(input())
    yyy1 = float(input())
    rrrr = float(input())
    xxx2 = float(input())
    yyy2 = float(input())
    print(
        "Yes" if ((xxx1 - xxx2)**2 + (yyy1 - yyy2)**2)**0.5 <= rrrr else "No"
    )
main()
