""" _ """

def main():
    """ _ """
    iii = input()
    counter = 0
    for j in range(2, len(iii)):
        for i in range(0, len(iii) - (j - 1)):
            ccc = 0
            for k in range(j):
                ccc += int(iii[k + i])
                if ccc > 10:
                    break
            if 10 == ccc:
                counter += 1
    print(counter)
main()
