""" _ """


def main():
    """ _ """

    rank = 0
    prev = 0
    share = 0
    for item in sorted(sorted(sorted([[(x if i == 0 else int(x))
                                       for (i, x) in enumerate(input().split(' '))]
                                      for _ in range(int(input()))], key=lambda x:
                                     sum(x[1:]), reverse=True), key=lambda x: x[0]),
                       key=lambda x: tuple(x[1:]), reverse=True):
        score_sum = sum(item[1:])
        score = ' '.join([str(x) for x in item[1:]])
        if score != prev:
            rank += share + 1
            share = 0
        elif rank != 0:
            share += 1
        print(rank, item[0], score, score_sum)
        prev = score


main()
