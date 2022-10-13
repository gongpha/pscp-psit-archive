""" _ """
def main():
    """ _ """
    students = []
    while True:
        line = input()
        if line == "END":
            break
        students.append(line[:4]) # dontcare after 4th char
    prev = 0
    for sss in sorted(set(students)):
        year = sss[:2]
        print(
            "--" if year == prev else year,
            int(sss[2:4]),
            students.count(sss)
        )
        prev = year
main()
