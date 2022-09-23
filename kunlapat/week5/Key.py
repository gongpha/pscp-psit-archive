"""do somthing"""

def main() -> int:
    """why the hell do I need to write this anyway?"""
    id_number = str(input())

    key = sum([*map(int, id_number)]) + int(id_number[-3:])*10

    print(key + 1000 if key <= 999 else str(key % 10000).rjust(4, "0"))

    return 0

if __name__ == "__main__":
    main()
