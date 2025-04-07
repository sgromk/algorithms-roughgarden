import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):

    def test_quicksort(self):
        # Simple case
        result1 = quicksort([3,2,1])
        print(result1)
        self.assertEqual(result1, [1,2,3])

        # Empty case
        result2 = quicksort([])
        print(result2)
        self.assertEqual(result2, [])

        # One element csae
        result3 = quicksort([1])
        print(result3)
        self.assertEqual(result3, [1])

        # Medium length case
        result4 = quicksort([7,4,9,33,2,6])
        print(result4)
        self.assertEqual(result4, [2,4,6,7,9,33])

        # Already sorted case
        result5 = quicksort([1, 2, 3, 4, 5])
        print(result5)
        self.assertEqual(result5, [1, 2, 3, 4, 5])

        # Reverse sorted case
        result6 = quicksort([5, 4, 3, 2, 1])
        print(result6)
        self.assertEqual(result6, [1, 2, 3, 4, 5])

        # Case with duplicates
        result7 = quicksort([3, 1, 2, 2, 4, 1])
        print(result7)
        self.assertEqual(result7, [1, 1, 2, 2, 3, 4])

        # Larger case
        result8 = quicksort([100, 200, 50, 150, 300, 250, 75, 125, 175, 225])
        print(result8)
        self.assertEqual(result8, [50, 75, 100, 125, 150, 175, 200, 225, 250, 300])

        # Case with negative numbers
        result9 = quicksort([3, -2, 1, -5, 4, 0, -1])
        print(result9)
        self.assertEqual(result9, [-5, -2, -1, 0, 1, 3, 4])

        # Case with large numbers
        result10 = quicksort([1000000, 500000, 100000, 50000, 10000000, 2000000])
        print(result10)
        self.assertEqual(result10, [50000, 100000, 500000, 1000000, 2000000, 10000000])


if __name__ == "__ main__":
    unittest.main()