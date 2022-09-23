"""Industrial revolution and its consiquences"""


def main() -> int:
    """The main function"""
    events = str(input())
    for battle in [i+j for i, j in zip(event, event[1:])]:
        battle_eval(battle)

    return 0

if __name__ == "__name__":
    main()
