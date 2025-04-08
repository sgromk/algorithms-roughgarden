import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):

    def test_quicksort(self):
        # Simple case
        result1,sum1 = quicksort([3,2,1])
        print(f"{result1}, sum: {sum1}")
        self.assertEqual(result1, [1,2,3])
        self.assertEqual(sum1, 3)

        # Empty case
        result2, sum2 = quicksort([])
        print(f"{result2}, sum: {sum2}")
        self.assertEqual(result2, [])
        self.assertEqual(sum2, 0)

        # One element csae
        result3, sum3 = quicksort([1])
        print(f"{result3}, sum: {sum3}")
        self.assertEqual(result3, [1])
        self.assertEqual(sum3, 0)

        # Medium length case
        result4, sum4 = quicksort([7,4,9,33,2,6])
        print(f"{result4}, sum: {sum4}")
        self.assertEqual(result4, [2,4,6,7,9,33])
        self.assertEqual(sum4, 9)

        # Already sorted case
        result5, sum5 = quicksort([1, 2, 3, 4, 5])
        print(f"{result5}, sum: {sum5}")
        self.assertEqual(result5, [1, 2, 3, 4, 5])
        self.assertEqual(sum5, 10)

        # Reverse sorted case
        result6, sum6 = quicksort([5, 4, 3, 2, 1])
        print(f"{result6}, sum: {sum6}")
        self.assertEqual(result6, [1, 2, 3, 4, 5])
        self.assertEqual(sum6, 10)

        # Case with duplicates
        result7, sum7 = quicksort([3, 1, 2, 2, 4, 1])
        print(f"{result7}, sum: {sum7}")
        self.assertEqual(result7, [1, 1, 2, 2, 3, 4])
        self.assertEqual(sum7, 9)

        # Larger case
        result8, sum8 = quicksort([100, 200, 50, 150, 300, 250, 75, 125, 175, 225])
        print(f"{result8}, sum: {sum8}")
        self.assertEqual(result8, [50, 75, 100, 125, 150, 175, 200, 225, 250, 300])
        self.assertEqual(sum8, 23)

        # Case with negative numbers
        result9, sum9 = quicksort([3, -2, 1, -5, 4, 0, -1])
        print(f"{result9}, sum: {sum9}")
        self.assertEqual(result9, [-5, -2, -1, 0, 1, 3, 4])
        self.assertEqual(sum9, 12)

        # Case with large numbers
        result10, sum10 = quicksort([1000000, 500000, 100000, 50000, 10000000, 2000000])
        print(f"{result10}, sum: {sum10}")
        self.assertEqual(result10, [50000, 100000, 500000, 1000000, 2000000, 10000000])
        self.assertEqual(sum10, 9)


if __name__ == "__ main__":
    unittest.main()