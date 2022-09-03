"""PSCP"""
def main():
    """Regulation"""
    integer = int(input())
    floating = float(input())
    strings = input()
    print("%30d"% integer)
    print("%s"% str(integer).zfill(30))
    print("%.02f" % floating)
    print("%.12f" % floating)
    print("%40s"% strings)
main()
