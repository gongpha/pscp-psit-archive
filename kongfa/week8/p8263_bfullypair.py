""" _ """
def main():
    """ _ """
    raw = input()
    orphan = ""
    tested = ""
    for char in raw:
        if char in tested:
            continue
        if raw.count(char) % 2 != 0:
            orphan += char
        tested += char
    print("fully paired" if len(orphan) == 0 else orphan)
main()
