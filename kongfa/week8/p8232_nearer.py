""" _ """
def main():
    """ _ """
    alice = int(input())
    bob = int(input())
    cart = int(input())

    alice_dist = abs(cart - alice)
    bob_dist = abs(cart - bob)
    print(
        "Sundaes %d" % alice_dist if alice_dist == bob_dist else
        "Bob %d" % bob_dist if alice_dist > bob_dist else
        "Alice %d" % alice_dist
    )
main()
