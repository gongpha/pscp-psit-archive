"""Prints something to console"""


def main():
    """The main function"""

    start_here = 492137954293754252786 # milliseconds
    seconds = start_here // 1000
    start_here = start_here % 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    print(days, hours, minutes, seconds, start_here)

main()
