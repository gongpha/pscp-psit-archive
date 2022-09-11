""" _ """

def grade(score):
    """ calc grade """
    return (
        4.0 if score >= 95 else
        3.5 if score >= 90 else
        3.0 if score >= 85 else
        2.5 if score >= 80 else
        2.0 if score >= 75 else
        1.5 if score >= 70 else
        1.0 if score >= 65 else
        0.5 if score >= 60 else
        0.0
    )

def main():
    """ _ """
    count = int(input())

    summation = 0
    for _ in range(count):
        summation += grade(float(input()))

    print('%.2f' % (int(summation / count * 100.0) / 100.0))
main()
