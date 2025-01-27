import unittest
from karatsuba_multiplication import karatsuba_mult


class TestKaratsuba(unittest.TestCase):

    def test_karatsuba(self):
        # Using the in-lecture example
        result = karatsuba_mult(1234, 5678)
        self.assertEqual(result, 7006652)

        # Testing simple cases
        result2 = karatsuba_mult(1, 7)
        self.assertEqual(result2, 7)

        result3 = karatsuba_mult(0, 3)
        self.assertEqual(result3, 0)

        result4 = karatsuba_mult(50, 256)
        self.assertEqual(result4, 12800)

        # A few larger cases
        result5 = karatsuba_mult(31998, 6380)
        self.assertEqual(result5, 204147240)

        result6 = karatsuba_mult(59525, 962859)
        self.assertEqual(result6, 57314181975)

if __name__ == "__main__":
    unittest.main()