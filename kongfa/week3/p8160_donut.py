""" _ """
def main():
    """ _ """
    price = int(input())
    free_quota = int(input())
    free = int(input())
    want = int(input())

    pack = free_quota + free
    pack_count = want // pack
    left = want - pack_count * pack

    if left >= free_quota:
        pack_count += 1
        left = 0

    real_count = pack_count * free_quota + left
    real_receive = real_count + (pack_count * free)
    print(real_count * price, real_receive)
main()
