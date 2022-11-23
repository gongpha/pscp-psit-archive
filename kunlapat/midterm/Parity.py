"""Better than ever!"""
from functools import reduce

def bit_parity(bits: str, mode: str) -> str:
    """Add a parity bit to a string of binary"""
    one_bit_odd = bool(int(reduce(lambda i, j: int(i)+int(j), bits)) % 2)

    return bits + "0" if (not one_bit_odd and mode == "Even" or
                          one_bit_odd and mode == "Odd") else bits + "1"


if __name__ == "__main__":
    print(bit_parity(input(), input()))
    