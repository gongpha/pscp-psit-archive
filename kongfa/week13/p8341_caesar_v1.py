""" _ """


def main():
    """ _ """
    step = int(input())
    text = input()

    newstring = ""
    for i in text:
        if i.isalpha():
            if i.islower():
                i = ord(i) - ord('a')
                isupper = False
            else:
                i = ord(i) - ord('A')
                isupper = True
            i = (i + step) % 26

            if isupper:
                i = chr(i + ord('A'))
            else:
                i = chr(i + ord('a'))
        newstring += i
    print(newstring)

main()
