""" _ """
def main():
    """ _ """
    print(list({iii for sss in [
        [i + "S", i + "H", i + "D", i + "C"]
        for i in ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
    ] for iii in sss}.difference({str(input()) for _ in range(51)}))[0])
main()
