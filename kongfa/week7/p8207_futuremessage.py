""" _ """
def main():
    """ _ """
    text = input()
    if text.isnumeric():
        print('Number')
    elif text.isupper():
        print('Uppercase')
    elif text.islower():
        print('Lowercase')
    elif text[0].isupper():
        print('Title')
    elif text.isspace():
        print('Space')
    else:
        print('Other')
main()
