""" _ """


def main():
    """ _ """
    price = int(input())
    cap_quota = int(input())
    new_price = int(input())
    want = int(input()) - 1

    print(
        (want + 1) * price if cap_quota == 0 else
        0 if want == -1 else
        price + ((
            want // cap_quota
        ) * ((price * (cap_quota - 1)) + new_price)) + ((
            want % cap_quota
        ) * price)
    )


main()
