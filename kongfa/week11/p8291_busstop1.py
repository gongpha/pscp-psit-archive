""" _ """


def main():
    """ _ """
    pas = int(input())
    done = 0
    pas_list = []
    seq = []
    for _ in range(1, int(input()) + 1):
        passs = input().split()
        stopidx = int(passs[0])
        seq.append((stopidx, passs[1:]))
    seq.sort(key=lambda x: x[0])
    for i in seq:
        done += pas_list.count(i[0])
        pas_list = [x for x in pas_list if x != i[0]]
        for ppp in i[1]:
            if int(ppp) < i[0]:
                continue
            if len(pas_list) >= pas:
                break
            pas_list.append(int(ppp))
    print(done)


main()
