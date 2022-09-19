""" _ """
def main():
    """ use list anyway """
    sequence = input()
    ppp = []
    temp = ''
    for char in sequence:
        if char == ' ':
            ppp += [temp] # Ez AVOIDING
            temp = ''
        else:
            temp += char
    if temp:
        ppp += [temp]

    # amen
    where_is_sun = ppp.index('Sun')
    print(
        'Hot: %s\nCool: %s' % (ppp[1], ppp[-1]) if ppp[0] == 'Sun' else
        'Hot: %s\nCool: %s' % (ppp[-2], ppp[0]) if ppp[-1] == 'Sun' else
        'Hot: %s %s' % (ppp[where_is_sun - 1], ppp[where_is_sun + 1]) +
        (
            '\nCool: %s %s' % (ppp[0], ppp[-1])
            if abs(ppp.index(ppp[0]) - where_is_sun) == abs(ppp.index(ppp[-1]) - where_is_sun) else
            '\nCool: %s' % ppp[0]
            if abs(ppp.index(ppp[0]) - where_is_sun) > abs(ppp.index(ppp[-1]) - where_is_sun) else
            '\nCool: %s' % ppp[-1]
        )
    )
main()
