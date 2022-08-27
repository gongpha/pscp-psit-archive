""" _ """
def main():
    """ _ """
    name = input()
    age = input()

    if age.isnumeric():
        age = int(age)
    else:
        age = 0

    print(
        (name + ", you can pass.") if age < 18 else
        (name + ", you shall not pass.")
    )

main()
