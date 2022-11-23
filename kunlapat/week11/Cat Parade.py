"""wszdniolNpigzijkmpD"KIFdfrz'lkf"""


def cat_parade() -> int:
    """hrdiuogfsbdaszhgfnsoijpgra"""
    prompt = input()
    raw_parade = []
    while prompt != "END":
        if prompt == "IT'S A DOG":
            raw_parade.pop(-1)
        else:
            for i in prompt.split(", "):
                raw_parade.append(i)
        # poll user prompt
        prompt = input()

    parade_sorted = sorted([*set(raw_parade)])

    for cat in parade_sorted:
        print("{} {} {}".format(cat, raw_parade.index(cat)+1, raw_parade.count(cat)))
    return 0

if __name__ == "__main__":
    cat_parade()
