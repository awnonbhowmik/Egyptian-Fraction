from fractions import Fraction as frac

def EgyptianFraction(n):
    if n <= 0 or n >= 1:
        raise Exception("Out of range", n)

    denom_lst = []

    while True:
        if n.numerator == 1:
            denom_lst.append(n)
            return denom_lst

        x = frac(1, int(float(n.denominator) / n.numerator+1))
        denom_lst.append(x)

        n -= x

    return denom_lst


a, b = input("Enter numerator and denominator a/b : ").split()
# a,b=int(a),int(b)
n = frac(int(a), int(b))

print(EgyptianFraction(n))