"""wegajoiernafdslkmxbg"""


def main() -> int:
    """erhjoidtgnlkf"""
    prompt = input()  # the first input poll
    menu = []
    while prompt != "DONE" or "CLOSED":
        # input handler
        if "Can't do:" in prompt:
            pass
        elif prompt == "SOMETHING'S WRONG":
            pass
        else:
            splited_prompt = prompt.split(" #")
            print(splited_prompt)
            if splited_prompt[-1] == "N":
                menu.append(splited_prompt[0])
            else:
                menu.insert(splited_prompt[-1], int(splited_prompt[0]))

    # TODO: DONE/CLOSE HANDLING

    # print result
    print("Full Course: {} Reversed: {}".format(str(menu), str(reversed(menu))))
    
    return 0

if __name__ == "__main__":
    main()