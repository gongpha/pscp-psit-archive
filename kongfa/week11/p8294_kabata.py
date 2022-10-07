""" _ """


def main():
    """ _ """
    print("\n".join([
        "yes" if (
            input()
            .replace("baka", "\001")  # sus
            .replace("bakka", "")
            .replace("ta", "")
            .replace("ba", "")
            .replace("ka", "") == ""
        ) else "no"
        for _ in range(int(input()))
    ]))


main()
