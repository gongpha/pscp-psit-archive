"""Do somthhings idk xdcc mkkas ls ba lkf"""

def main() -> int:
    """The manin fucntor"""
    target = int(input())
    var_in, var_out = 0, 0
    while True:
        var_in = int(input())
        if var_in == -1:
            break
        var_out += var_in
        if var_out == target:
            break

    print(var_out)

    return 0

if __name__ == "__main__":
    main()
