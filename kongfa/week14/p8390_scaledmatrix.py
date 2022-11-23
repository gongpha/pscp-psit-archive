""" _ """
def main():
    """ _ """
    mmm = int(input())
    nnn = int(input())
    matrix = []
    for _ in range(mmm):
        matrix.append([float(input()) for i in range(nnn)])
    flatten = [j for i in matrix for j in i]
    minv = min(flatten)
    maxv = max(flatten)
    for rrr in matrix:
        print(' '.join(
            '%.2f' % float((x - minv) / (maxv - minv)) for x in rrr
        ))

main()
