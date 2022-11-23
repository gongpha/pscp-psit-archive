""" _ """

def main():
    """ _ """
    band = {
        'Black': 0,
        'Brown': 1,
        'Red': 2,
        'Orange': 3,
        'Yellow': 4,
        'Green': 5,
        'Blue': 6,
        'Purple': 7,
        'Grey': 8,
        'White': 9
    }
    mul = {
        'Black': 1,
        'Brown': 10,
        'Red': 100,
        'Orange': 1000,
        'Yellow': 10000,
        'Green': 100000,
        'Blue': 1000000,
        'Purple': 10000000,
        'Gold': 0.1,
        'Silver': 0.01
    }
    tol = {
        'Brown': 1,
        'Red': 2,
        'Green': 0.5,
        'Blue': 0.25,
        'Purple': 0.1,
        'Grey': 0.05,
        'Gold': 5,
        'Silver': 10
    }
    iii_band1 = band.get(input(), None)
    iii_band2 = band.get(input(), None)
    iii_mul = mul.get(input(), None)
    iii_tol = tol.get(input(), None)
    if any(map(lambda x: x is None, (iii_band1, iii_band2, iii_mul, iii_tol))):
        print('Error')
        return
    summ = int(str(iii_band1) + str(iii_band2))
    lll = summ*iii_mul
    rrr = (summ*iii_mul)*(iii_tol/100)
    print('%.4f' % (lll - rrr))
    print('%.4f' % (lll + rrr))
main()
