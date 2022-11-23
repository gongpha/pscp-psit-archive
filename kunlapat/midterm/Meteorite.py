"""Infact, I have not improved at all"""


def meteorite(weight: float, split: int, threshold: float) -> int:
    """Calculate the amount of missiles it will take to reduce the meteorite..."""
    if weight < threshold:
        return 0
    else:
        missiles, splits = 1, 1
        weight /= split
        while weight >= threshold:
            missiles += split**splits
            weight /= split
            splits += 1
        return missiles

if __name__ == "__main__":
    print(meteorite(float(input()), int(input()), float(input())))
