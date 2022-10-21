""" _ """
def main():
    """ _ """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weektext = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = int(input())
    month = int(input())
    week = 5

    for i in range(month):
        for j in range(days[i]):
            if i + 1 == month:
                if j + 1 == day:
                    print(weektext[week])
                    return
            week = (week + 1) % 7


main()
