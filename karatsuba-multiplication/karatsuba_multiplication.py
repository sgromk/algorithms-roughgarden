def karatsuba_mult(multiplicand, multiplier):
    """
    Performs Karatsuba multiplication on two numbers.

    Args:
        multiplicand (int): The first number being multiplied.
        multiplier (int): The second number being multiplied.

    Returns:
        int: The product of the two given numbers.
    """
    if multiplicand < 10 and multiplier < 10:
        return multiplicand * multiplier

    # Convert int inputs to strings
    multiplicand = str(multiplicand)
    multiplier = str(multiplier)

    max_len = max(len(multiplicand), len(multiplier))
    multiplicand = multiplicand.zfill(max_len)
    multiplier = multiplier.zfill(max_len)

    n = len(multiplicand)
    m = (n+1) // 2

    print(f"n: {n}, m: {m}")
    
    a = multiplicand[:m]
    b = multiplicand[m:]
    c = multiplier[:m]
    d = multiplier[m:]


    ac = karatsuba_mult(int(a), int(c))
    bd = karatsuba_mult(int(b), int(d))



    aPlusB = int(a) + int(b)
    cPlusD = int(c) + int(d)

    ab_cd = karatsuba_mult(aPlusB, cPlusD)

    ad_bc = ab_cd - ac - bd

    return ac * 10 ** (2 * (n - m)) + ad_bc * 10 ** (n-m) + bd


if __name__ == '__main__':

    # Using the two given numbers for the problem set.
    num1 = 12
    num2 = 34

    print(karatsuba_mult(num1, num2))