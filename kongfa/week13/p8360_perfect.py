""" _ """
def main():
    """ _ """
    print(sum([
        i for i in range(2, int(input()), 2) if (sum(
            {1} | {k for l in {
                (i//j, j) for j in range(2, int(-1*(i**0.5)//1*-1)+1) if i % j == 0
            } for k in l}
        )) == i
    ]))
main()
