"""I am done with my bullshit, the test is tomorrow"""


def bounce(height: float) -> int:
    """Count the bounces of a ball given height"""
    bounces = 0
    while True:
        height = height * 3 / 5
        if height < 0.01:
            break
        bounces += 1
    return bounces

if __name__ == "__main__":
    print(bounce(float(input())))
