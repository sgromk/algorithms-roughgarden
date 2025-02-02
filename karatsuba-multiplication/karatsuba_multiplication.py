from math import ceil

def karatsuba_mult(multiplicand, multiplier):
    """
    Performs Karatsuba multiplication on two numbers.

    Args:
        multiplicand (int): The first number being multiplied.
        multiplier (int): The second number being multiplied.

    Returns:
        int: The product of the two given numbers.
    """
    if multiplicand < 10 or multiplier < 10:
        return multiplicand * multiplier

    n = max(len(str(multiplicand)), len(str(multiplier)))
    m = ceil(n/2)

    a = multiplicand // (10 ** m)
    b = multiplicand % (10 ** m)
    c = multiplier // (10 **m)
    d = multiplier % (10 ** m)


    ac = karatsuba_mult(int(a), int(c))
    bd = karatsuba_mult(int(b), int(d))



    aPlusB = int(a) + int(b)
    cPlusD = int(c) + int(d)

    ab_cd = karatsuba_mult(aPlusB, cPlusD)

    ad_bc = ab_cd - ac - bd

    print(f"a: {a}, b: {b}, c: {c}, d: {d}, n: {n}, m: {m}")

    return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd