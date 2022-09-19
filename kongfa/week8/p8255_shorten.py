""" _ """
def main():
    """ _ """
    buffer = ""

    start = -1
    end = -1
    nextnum = -1
    count = 0
    break_later = False
    while True:
        if nextnum != -1:
            innum = nextnum
            nextnum = -1
        else:
            innum = int(input())
            if innum == -1:
                break_later = True

        if start == -1:
            start = innum
            end = innum
        else:
            if abs(end - innum) > 1:
                if count:
                    buffer += ('' if len(buffer) == 0 else ', ') + '%d-%d' % (start, end)
                else:
                    buffer += ('' if len(buffer) == 0 else ', ') + str(end)
                start = -1
                end = -1
                nextnum = innum
                count = 0
            else:
                end = innum
                count += 1
        if break_later:
            break
    print(buffer)
main()
