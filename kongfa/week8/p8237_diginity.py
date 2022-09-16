""" _ """
def main():
    """ _ """
    result = 0
    output = ""
    while True:
        nnn = int(input())
        if nnn == 0:
            break

        while nnn >= 10:
            result = 0
            for char in str(nnn):
                result += int(char)
            nnn = result
        output += ("" if len(output) == 0 else "\n") + str(nnn)

    print(output)
main()
