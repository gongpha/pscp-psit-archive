""" _ """
def main():
    """ _ """
    seconds = int(input())
    c_seconds = int(input())
    c_minutes = int(input())
    c_hours = int(input())
    seconds = seconds % (c_hours*c_minutes*c_seconds)
    hours = seconds // (c_minutes*c_seconds)
    seconds = seconds % (c_minutes*c_seconds)
    minutes = seconds // c_seconds
    seconds = seconds % c_seconds
    print("%d:%d:%d" % (hours, minutes, seconds))
main()
