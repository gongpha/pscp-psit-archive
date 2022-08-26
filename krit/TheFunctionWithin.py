"""Prints something to console"""


def main() -> int:
    """The main function"""
    temp = []
    func_f = lambda x: 2*x
    func_g = lambda x: (3*(x**4))-(x**3)+(2*(x**2))+10
    func_h = lambda x, y, z: ((z + x)**2) - (x*y) + (y**2)
    func_i = lambda a, b, c, d: ((a**2)+(b**2)-(c**2))/((d**2)-(2*a*d)+(2*a))
    temp.append(float(input()))
    temp.append(float(input()))
    temp.append(float(input()))
    temp.append(float(input()))
    print(func_f(func_f(temp[0])))
    print(func_g(func_f(temp[0]-temp[1])))
    print(func_h(func_f(temp[0]+temp[1]),
                 func_f(temp[0]+temp[2]), func_g(func_f(temp[3]**2))))
    print(func_i(func_h(func_f(temp[0]+temp[1]), func_f(temp[0]-temp[2]),
                        func_g(func_f(temp[3]**2))),
                 func_g(func_f(temp[0]-temp[1])),
                 func_f(func_f(func_f(func_f(func_f(temp[2])
                                            )))), temp[3]**8))
    return 0


if __name__ == "__main__":
    main()
