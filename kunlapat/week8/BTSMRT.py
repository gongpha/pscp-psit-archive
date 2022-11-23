"""fgretfrhgjh"""


def pay_or_free(day_type: str, age: float, height: float) -> str:
    """cfvghb nj,km."""
    return "FREE" if (age < 14 and height < 90 or
                      day_type == "Children Day" and age < 14 and height < 140 or
                      day_type == "Senior Day" and age > 60) else "PAY"


if __name__ == "__main__":
    print(pay_or_free(input(), float(input()), float(input())))
