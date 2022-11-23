"""I'm back, baby!"""

def triangle_area_from_sides(side_a: float,
                             side_b: float,
                             side_c: float) -> float:
    """Calculate the area of a triangle from the length of its sides"""
    const_s = (side_a+side_b+side_c)/2
    return (const_s*(const_s-side_a)*(const_s-side_b)*(const_s-side_c))**0.5

if __name__ == "__main__":
    print("%.3f" % triangle_area_from_sides(float(input()), float(input()), float(input())))
