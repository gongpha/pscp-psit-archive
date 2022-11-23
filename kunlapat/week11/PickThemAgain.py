"""gfdrnbdnfsgreagsdg"""


def print_list(esgzrhedtfjyh: str) -> str:
    """wefgrhonkclmfdsezgdhnok"""
    gsfdxgb = list(reversed(list(filter(
        lambda x: int(x)%3 == 0 or int(x)%5 == 0,
        esgzrhedtfjyh.split(" ")
    ))))

    return "\n".join(gsfdxgb) if len(gsfdxgb) != 0 else "Nope"

if __name__ == "__main__":
    print(print_list(input()))

