""" _ """
def main():
    """ _ """
    romantable = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = input()
    print(sum([
        romantable[roman[i]] - (
            2 * romantable[roman[i - 1]] if (
                i > 0 and romantable[roman[i]] > romantable[roman[i - 1]]
            ) else 0)
        for i in range(len(roman))
    ]))
main()