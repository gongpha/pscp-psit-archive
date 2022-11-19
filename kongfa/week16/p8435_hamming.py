""" _ """
def main():
    """ _ """
    aa1 = input()
    aa2 = input()
    diff = 0
    for iii, _ in enumerate(aa1):
        if aa2[iii] != aa1[iii]:
            diff += 1
    print(diff)

main()
