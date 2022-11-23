""" _ """

def main():
    """ _ """
    eggs = []
    for _ in range(int(input())):
        nnn, ppp, qqq = tuple(map(int, input().split()))
        www = sorted(map(float, input().split()))
        weight = 0
        egg = 0
        for i in range(min(nnn, ppp)):
            weight += www[i]
            if weight > qqq:
                break
            egg += 1
        eggs.append(egg)
    print('\n'.join(map(str, eggs)))
main()
