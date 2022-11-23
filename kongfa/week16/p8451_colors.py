""" _ """
def main():
    """ _ """
    colmap = {
        'Red' : (1, 0, 0),
        'Yellow' : (0, 1, 0),
        'Blue' : (0, 0, 1),
        'Orange' : (1, 1, 0),
        'Violet' : (1, 0, 1),
        'Green' : (0, 1, 1),
    }
    col1 = input()
    col2 = input()
    if any(map(lambda x: x not in ('Red', 'Yellow', 'Blue'), (col1, col2))):
        print('Error')
        return
    col1 = colmap.get(col1, None)
    col2 = colmap.get(col2, None)
    col3 = (
        min(1, col1[0] + col2[0]),
        min(1, col1[1] + col2[1]),
        min(1, col1[2] + col2[2]),
    )
    for key, value in colmap.items():
        if value == col3:
            print(key)
            return
    print('Error')
main()
