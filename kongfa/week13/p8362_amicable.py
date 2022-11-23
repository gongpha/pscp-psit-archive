""" _ """
def pdiv(i):
    """ _ """
    return sum(
        {1} | {k for l in {
            (i//j, j) for j in range(2, int(-1*(i**0.5)//1*-1)+1) if i % j == 0
        } for k in l}
    )

def main():
    """ _ """
    total = 0
    for i in range(1, int(input()), 1):
        ppp = pdiv(i)
        total += i if i == pdiv(ppp) and ppp != i else 0
    print(total)

main()
