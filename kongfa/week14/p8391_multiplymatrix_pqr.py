""" _ """
def main():
    """ _ """
    ppp = int(input())
    qqq = int(input())
    rrr = int(input())

    matrix1 = []
    for _ in range(ppp):
        matrix1.append([int(input()) for i in range(qqq)])

    matrix2 = []
    for _ in range(qqq):
        matrix2.append([int(input()) for i in range(rrr)])

    matrix3 = []
    for i, _ in enumerate(matrix1):
        matrix3.append([])
        for j in range(len(matrix2[0])):
            matrix3[i].append(0)
            for k, _ in enumerate(matrix2):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
    print('\n'.join(
        ' '.join(map(str, rrr))
        for rrr in matrix3
    ))
main()
