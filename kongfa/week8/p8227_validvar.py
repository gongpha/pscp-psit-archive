""" _ """

def main():
    """ _ """
    punctuations = "!\"#$%&'()*+, -./:;<=>?@\\^`{|}~"
    count = int(input())
    output = ""
    for _ in range(count):
        count -= 1
        keyword = input()
        valid = True
        if valid:
            # 3 4
            valid = keyword.isidentifier() and not (
                # "tupl​e"s are restricted BUT '(' and ')' are not.
                # unsafe things lol
                keyword == "if" or
                keyword == "else" or
                keyword == "elif" or
                keyword == "while" or
                keyword == "for" or
                keyword == "True" or
                keyword == "False" or
                keyword == "continue" or
                keyword == "break" or
                keyword == "return" or
                keyword == "is" or
                keyword == "in" or
                keyword == "and" or
                keyword == "or" or
                keyword == "from" or
                keyword == "as" or
                keyword == "pass" or
                keyword == "not" or
                keyword == "def" or
                keyword == "None"
            )
        if valid:
            # 1 2
            for char in keyword:
                if char in punctuations or char.isspace():
                    valid = False
                    break
        output += ("Valid" if valid else "Invalid") + ('' if count == 0 else '\n')
    print(output)
main()
