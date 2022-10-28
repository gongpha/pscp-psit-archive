""" _ """
def main():
    """ _ """
    nnn = int(input())
    points = [
        tuple(map(int, input().split()))
        for _ in range(nnn)
    ]
    print('%.2f' % (
        sum(
            ((points[i][0] - points[i + 1][0])**2 + (points[i][1] - points[i + 1][1])**2)**0.5
            for i in range(nnn - 1)
        )
    ))

main()
