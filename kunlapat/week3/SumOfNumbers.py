"""Do somthhings idk xdcc mkkas ls ba lkf"""

def getln_sum(var_in: int, prev_var: int, target: int) -> int:
    usr_input = var_in - prev_var
    if usr_input == -1:
        return var_in
    elif var_in == target:
        return var_in
    else:
        return  getln_sum(int(input()) + usr_input, usr_input, target)


def main() -> int:
    """The manin fucntor"""
    target = int(input())
    # var_in, var_out = 0, 0
    # while True:
    #     var_in = int(input())
    #     if var_in == -1:
    #         break
    #     var_out += var_in
    #     if var_out == target:
    #         break

    print(getln_sum(int(input()), 0, target))

    return 0

if __name__ == "__main__":
    main()
