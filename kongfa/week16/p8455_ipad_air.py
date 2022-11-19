""" _ """
def main():
    """ _ """
    color = input()
    storage = int(input())
    connection = input()
    print(
        'Not Available' if (
            color not in ('Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue') or
            storage not in (64, 256) or
            connection not in ('Wi-Fi', 'Wi-Fi + Cellular')
        )
        else
        19900 +
        (4500 * int(connection == 'Wi-Fi + Cellular')) +
        (5000 * int(storage == 256))
    )
main()
