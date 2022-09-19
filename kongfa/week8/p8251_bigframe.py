""" _ """
def main():
    """ _ """
    lll1 = input().rstrip()
    lll2 = input().rstrip()
    lll3 = input().rstrip()
    lll4 = input().rstrip()
    lll5 = input().rstrip()

    maxlen = max(len(lll1), len(lll2), len(lll3), len(lll4), len(lll5))
    print(
        "*" * (maxlen + 4) + "\n" +
        "* %0s *\n" % lll1.ljust(maxlen) +
        "* %0s *\n" % lll2.ljust(maxlen) +
        "* %0s *\n" % lll3.ljust(maxlen) +
        "* %0s *\n" % lll4.ljust(maxlen) +
        "* %0s *\n" % lll5.ljust(maxlen) +
        "*" * (maxlen + 4) + "\n"
    )
main()
