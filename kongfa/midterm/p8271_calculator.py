""" _ """
def main():
    """ _ """
    xxx = int(input())
    if xxx == 1:
        print(1)
        return
    hit = 1 + (xxx - 1)
    while xxx:
        hit += len(str(xxx))
        xxx -= 1
    print(hit)
main()
