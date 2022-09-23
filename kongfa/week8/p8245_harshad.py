""" _ """
def main():
    """ _ """
    output = ""
    for i in range(10):
        nnn = input().replace('-', '')
        total = 0
        for char in nnn:
            total += int(char)
        output += "No" if total == 0 or int(nnn) % total != 0 or int(nnn) == 0 else "Yes"
        if i != 9:
            output += "\n"
    print(output)
main()
