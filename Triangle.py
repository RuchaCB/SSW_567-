def validate (a):
    try:
        a = float(a)
        return True
    except ValueError:
        return False


def triangles(a,b,c):
    
    final = []
    if a==0 or b==0 or c==0:
        return ("Enter non-zero values")
    elif validate(a)==True and validate(b)==True and validate(c)==True:
        A = a**2
        B = b**2
        C = c**2

        if a==b and b==c:
            final.append("Equilateral Triangle")

        if a==b or b==c or a==c:
            final.append("Isosceles Triangle")

        if a!=b and b!=c and a!=c:
            final.append("Scalene Triangle")

        if (A+B) == C:
            final.append("Right Angle Triangle")
        elif (C+B)==A:
            final.append("Right Angle Triangle")
        elif (C+A)==B:
            final.append("Right Angle Triangle")        
    
    else:
        final.append("Enter a valid set of inputs")

    return final

        
