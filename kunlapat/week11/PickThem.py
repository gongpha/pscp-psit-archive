"""gfdrnbdnfsgreagsdg"""
import json


def print_list(input: str) -> str:
    """wefgrhonkclmfdsezgdhnok"""
    input_even = list(map(str, list(filter(lambda x: int(x)%2 == 0, json.loads(input)))))

    return "\n".join(input_even) if len(input_even) != 0 else "Nope"

if __name__ == "__main__":
    print(print_list(input()))
