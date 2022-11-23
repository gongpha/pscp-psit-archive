""" _ """
def main():
    """ _ """
    text = input().split()
    numdict = {
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'eleven':11,
        'twelve':12,
        'thirteen':13,
        'fourteen':14,
        'fifteen':15,
        'sixteen':16,
        'seventeen':17,
        'eighteen':18,
        'nineteen':19,
        'twenty':20,
        'thirty':30,
        'forty':40,
        'fifty':50,
        'sixty':60,
        'seventy':70,
        'eighty':80,
        'ninety':90,
        'hundred':100,
        'thousand':1000
    }

    text.reverse()
    num = 0

    keep = 0

    for ttt in text:
        if ttt in ['hundred', 'thousand']:
            keep = numdict[ttt]
        else:
            mul = 1
            if keep != 0:
                mul = keep
            num += numdict[ttt] * mul
    print(len(str(num)))

main()
