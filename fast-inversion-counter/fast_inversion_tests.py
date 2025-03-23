import unittest
from fast_inversion_counter import fast_inv_count

class TestFastInvCount(unittest.TestCase):

    def test_fast_inv_count(self):
        # Typical 2^n case (all even splits)
        result1 = fast_inv_count([2, 5, 7, 1, 3, 8, 10, 4])
        self.assertEqual(result1, 9)

        # Case containing odd splits
        result2 = fast_inv_count([15, 23, 8, 42, 16, 5, 34, 9, 11, 50, 28])
        self.assertEqual(result2, 23)

        # Empty case
        result3 = fast_inv_count([])
        self.assertEqual(result3, 0)

        # Single element case
        result4 = fast_inv_count([42])
        self.assertEqual(result4, 0)


if __name__ == "__main__":
    unittest.main()