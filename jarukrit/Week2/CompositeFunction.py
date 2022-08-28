"""Prints something to console"""


def main() -> int:
    """The main function"""
    func_f = lambda x: 2*x
    func_g = lambda x: x/2 + 1
    num = float(input())
    print("%.2f" % func_f(func_g(num)))
    print("%.2f" % func_g(func_f(num)))
    return 0

if __name__ == "__main__":
    main()
