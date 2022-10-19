"""Industrial revolution and its consiquences"""


def swap(table: list, action: str) -> list:
    """Swap elements of table according to the action"""
    if action == "A":
        table[0], table[1] = table[1], table[0]
    elif action == "B":
        table[1], table[2] = table[2], table[1]
    elif action == "C":
        table[0], table[2] = table[2], table[0]
    return table

def main() -> int:
    """The main function"""
    events = str(input())
    forif = [1, 0, 0]
    for action in events:
        forif = swap(forif, action)

    print(forif.index(1)+1)

    return 0

if __name__ == "__main__":
    main()
