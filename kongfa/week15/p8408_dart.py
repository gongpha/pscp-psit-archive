""" _ """
def main():
    """ _ """
    nnn = int(input())
    score = 0
    for _ in range(nnn):
        coord = list(map(int, input().split()))
        radius = (coord[0]**2 + coord[1]**2) ** 0.5
        if radius <= 2:
            score += 5
        elif radius <= 4:
            score += 4
        elif radius <= 6:
            score += 3
        elif radius <= 8:
            score += 2
        elif radius <= 10:
            score += 1
    print(score)
main()
