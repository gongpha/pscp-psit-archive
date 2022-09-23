""" _ """

def main():
    """ _ """
    nnn = int(input())
    kkk = int(input())
    xxx = int(input())
    yyy = int(input())
    day = 0
    read = 0
    readbook = 0
    while True:
        if readbook == nnn:
            break
        read_each = int(-1 * (
            ((xxx + day) / (yyy + day)) * kkk
        ) // 1 * -1)
        if read_each >= kkk:
            break
        read += read_each
        day += 1

        if read >= kkk:
            read = 0
            readbook += 1
    print(day + (nnn - readbook))

main()
