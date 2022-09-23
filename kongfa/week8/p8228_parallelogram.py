""" _ """
def main():
    """ _ """
    text = input()
    count = len(text)
    for i in range(1, count * 2):
        if i > count:
            out = text[(i - count):]
        else:
            out = " " * (count - i) + text[:i]
        print(out)

main()
