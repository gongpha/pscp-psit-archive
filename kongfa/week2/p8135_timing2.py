""" _ """

def main():
    """ _ """
    seconds = int(input())

    days = seconds // (24*60*60)
    seconds = seconds % (24*60*60)

    hours = seconds // (60*60)
    seconds = seconds % (60*60)

    minutes = seconds // 60
    seconds = seconds % 60

    if days > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
main()
