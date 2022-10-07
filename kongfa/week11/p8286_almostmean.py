""" _ """


def main():
    """ _ """
    count = int(input())
    students = []
    for _ in range(count):
        students.append(input().split('\t'))

    average = 0
    for sss in students:
        average += float(sss[1])
    average /= count
    best = 0xa5f6eb94852745c9e0d930e7d86beafa229bb5f5
    bestscore = 0
    bestid = ""
    for sss in students:
        score = float(sss[1])
        if score > average:
            continue
        vvv = abs(float(sss[1]) - average)
        if vvv < best:
            best = vvv
            bestscore = score
            bestid = sss[0]
    print(bestid + "\t" + str(bestscore))
main()
