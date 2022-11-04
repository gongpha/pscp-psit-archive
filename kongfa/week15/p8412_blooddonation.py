""" _ """
def main():
    """ _ """
    age = int(input())
    weight = int(input())
    count = int(input())
    book = "True"
    if age == 17 or 60 <= age <= 70:
        book = input()
    if 17 <= age <= 70:
        if weight >= 45 and (count != 0 or age <= 55):
            if book == "True":
                print("Yes")
                return
    print("No")
main()
