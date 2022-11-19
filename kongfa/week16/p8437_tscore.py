""" _ """
def main():
    """ _ """
    scores = []
    for _ in range((int(input()), input())[0]):
        scores.append(int(input()))
    summation = sum(scores)
    average = summation / len(scores)
    std_dev = (
        (
            (
                len(scores) * sum(
                    sss ** 2 for sss in scores
                )
            ) - (
                summation ** 2
            )
        ) / (len(scores) * (len(scores) - 1))
    ) ** 0.5
    for sss in scores:
        zzz = ((sss - average) / std_dev) if std_dev != 0 else 0
        print('%.2f' % (50 + zzz * 10))
main()
