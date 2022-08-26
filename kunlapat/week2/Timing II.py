"""Converts seconds into a timestamp"""


def main() -> int:
    """The main function"""
    input_second = int(input())

    output_day = input_second//86400
    output_hour = (input_second-86400*output_day)//3600
    output_minute = (input_second-86400*output_day-3600*output_hour)//60
    output_second = input_second-86400*output_day-3600*output_hour-60*output_minute

    if output_day < 10000:
        print("{:04d}:{:02d}"
              ":{:02d}:{:02d}".format(output_day,
                                      output_hour, output_minute, output_second))
    else:
        print("ERR_:__:__:__")

    return 0

if __name__ == "__main__":
    main()
