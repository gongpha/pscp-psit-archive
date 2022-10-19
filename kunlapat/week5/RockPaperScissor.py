"""Industrial revolution and its consiquences"""


def play(game: str) -> str:
    """Play a game of rock paper scissor. return winner, d if draw"""
    return "a" if game == "PR" or game == "RS" or game == "SP" else "d" if game.count(game[0]) == 2 else "b"
    
def main() -> int:
    """The main function"""
    events = str(input())
    point_a, point_b = 0, 0
    for i in range(0, len(events), 2):
        if play(events[i] + events[i+1]) == "a":
            point_a += 1
        elif play(events[i] + events[i+1]) == "b":
            point_b += 1

    if point_a > point_b:
        print(f"A win {point_a}-{point_b}")
    elif point_a < point_b:
        print(f"B win {point_b}-{point_a}")
    else:
        print(f"DRAW {point_a}")
    
    return 0

if __name__ == "__main__":
    main()
