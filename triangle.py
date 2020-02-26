"""
Check the type of Triangles
"""
def validate(num):
    """To validate"""
    try:
        num = float(num)
        return True
    except ValueError:
        return False


def triangles(side_a, side_b, side_c):
    """Check Triangle"""
    final = []
    if side_a == 0 or side_b == 0 or side_c == 0:
        return "Enter non-zero values"
    if (validate(side_a) is True) and (validate(side_b) is True) and (validate(side_c) is True):
        new_a = side_a**2
        new_b = side_b**2
        new_c = side_c**2
        if side_a == side_b and side_b == side_c:
            final.append("Equilateral Triangle")
        if side_a == side_b or side_b == side_c or side_a == side_c:
            final.append("Isosceles Triangle")
        if side_a != side_b and side_b != side_c and side_a != side_c:
            final.append("Scalene Triangle")
        if (new_a+new_b) == new_c or (new_c+new_b) == new_a or (new_c+new_a) == new_b :
            final.append("Right Angle Triangle")
    else:
        return "Enter a valid set of inputs"
    return final
