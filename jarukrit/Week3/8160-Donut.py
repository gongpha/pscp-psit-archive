'''PSCP Program'''
def main():
    '''Donut'''
    price = int(input())
    bundle = int(input())
    free_from_bundle = int(input())
    minimum = int(input())
    donuts, pay, free_count, = 0, 0, 0
    if price + bundle + free_from_bundle + minimum > 10**7:
        donuts = minimum
        free_count += free_from_bundle * minimum//bundle
        pay = minimum*price
        while donuts+free_count > minimum:
            donuts -= 2560
            pay -= price*2560
            if donuts // bundle *free_from_bundle != free_count:
                free_count = donuts // bundle *free_from_bundle

        while donuts+free_count < minimum:
            donuts += 1
            pay += price
            if donuts // bundle *free_from_bundle != free_count:
                free_count = donuts // bundle *free_from_bundle
        print(pay, donuts+free_count)

    else:
        while donuts+free_count < minimum:
            donuts += 1
            pay += price
            if donuts % bundle == 0:
                free_count += free_from_bundle
        print(pay, donuts+free_count)

if __name__ == "__main__":
    main()
