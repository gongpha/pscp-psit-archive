""" _ """
def main():
    """ _ """
    day = int(input())
    month = int(input())
    day2 = int(input())
    month2 = int(input())

    month_yon = [
        4, 6, 9, 11
    ]

    if (month2 == 2 and day2 > 28)\
        or (month == 2 and day > 28) or\
            (day >= 31 and month in month_yon) or\
                (day2 >= 31 and month2 in month_yon):
        print("Impossible")
        return

    counter = 0

    day_total = month * 100 + day
    day2_total = month2 * 100 + day2

    if day_total > day2_total:
        day, day2 = day2, day
        month, month2 = month2, month
    while True:
        if day == day2 and month == month2:
            break
        counter += 1
        day += 1
        if month == 2:
            if day == 29:
                day = 1
                month += 1
        if month in month_yon:
            if day == 31:
                day = 1
                month += 1
        else:
            if day == 32:
                day = 1
                month += 1
    print(counter)
main()
