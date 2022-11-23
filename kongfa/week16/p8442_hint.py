""" _ """
def main():
    """ _ """
    iii = (input(), input(), input())
    vvv = [
        [j[1]] if j[0] == "==" else (
            [int(i) for i in range(0, 10) if i < j[1]]
            if j[0] == "<" else
            [int(i) for i in range(0, 10) if i <= j[1]]
            if j[0] == "<=" else
            [int(i) for i in range(0, 10) if i > j[1]]
            if j[0] == ">" else
            [int(i) for i in range(0, 10) if i >= j[1]]
            if j[0] == ">=" else
            [int(i) for i in range(0, 10) if i != j[1]]
        )
        for j in [(i.split()[0], int(i.split()[1])) for i in iii]
    ]
    for aa1 in vvv[2]:
        for aa2 in vvv[1]:
            for aa3 in vvv[0]:
                print(str(aa1) + str(aa2) + str(aa3))
main()
