'''PSCP Program'''
def main() -> int:
    '''GraderMachine'''
    out, count, step = "", 0, 1
    from_num, to_num = int(input()), int(input())
    if from_num > to_num:
        to_num -= 2
        step = -1
    for i in range(from_num, to_num+1, step):
        if (i % 2) == 0:
            if count == 0:
                out = str(i)
            else:
                out = out + " " + str(i)
            count += i
    print("pass :", out)
    print("Sum : %d" % count)
if __name__ == "__main__":
    main()
