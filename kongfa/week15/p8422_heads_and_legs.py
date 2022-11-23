""" _ """
def main():
    """ _ """
    total = int(input())
    rabbit = int(input()) / 2 - total
    print(*(
        (int(rabbit), int(total - rabbit)) if (
            rabbit >= 0 and total - rabbit >= 0 and\
            rabbit % 1 == 0 and (total - rabbit) % 1 == 0
        ) else
        ("Impossible",)
    ))

main()
