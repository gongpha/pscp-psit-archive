"""Take some input, does somthing idk"""

def main() -> int:
    """The main function"""
    init = int(input())
    end = int(input())
    jump = int(input())

    # Literally how I would do it in Haskell
    print("\n".join([str(x) for x in list(
        filter(lambda x: x < end, map(lambda x: init+jump*x, range(end)))
    )]))

    return 0

if __name__ == "__main__":
    main()
