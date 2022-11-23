""" _ """
def main():
    """ _ """
    text = input().lower().replace(" ", "")
    print(max(set(text), key=text.count))
main()
