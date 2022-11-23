""" _ """
def main():
    """ _ """
    aaa = list(map(int, input().split(' ')))
    bbb = list(map(int, input().split(' ')))
    xx1 = max(min(aaa[0], aaa[0] + aaa[2]), min(bbb[0], bbb[0] + bbb[2]))
    yy1 = max(min(aaa[1], aaa[1] + aaa[3]), min(bbb[1], bbb[1] + bbb[3]))
    xx2 = min(max(aaa[0], aaa[0] + aaa[2]), max(bbb[0], bbb[0] + bbb[2]))
    yy2 = min(max(aaa[1], aaa[1] + aaa[3]), max(bbb[1], bbb[1] + bbb[3]))
    print("no overlapping" if xx1 >= xx2 or yy1 >= yy2 else (
        (xx2 - xx1) * (yy2 - yy1)
    ))
main()
