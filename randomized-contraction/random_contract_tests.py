import unittest
from randomized_contraction import randomized_contraction

class test_randomized_contraction(unittest.TestCase):

    def test_rand_cont1(self):
        adjacency_list1 = [(1,2), (2,3), (3,1)]
        result1 = 2
        self.assertEqual(adjacency_list1, result1)

    def test_rand_cont2(self):
        adjacency_list2 = [(1,2), (2,3), (3,4), (4,1), (1,3)]
        result2 = 2
        self.assertEqual(adjacency_list2, result2)

    def test_rand_cont3(self):
        adjacency_list3 = [(1,2), (1,3), (1,4), (1,5)]
        result3 = 1
        self.assertEqual(adjacency_list3, result3)

    def test_rand_cont4(self):
        adjacency_list4 = [()]
        result4 = 1
        self.assertEqual(adjacency_list4, result4)

    def test_rand_cont5(self):
        adjacency_list5 = [(1,2), (2,3), (3,1), (4,5), (5,6), (6,4), (3,4)]
        result5 = 1
        self.assertEqual(adjacency_list5, result5)

    def test_rand_cont6(self):
        adjacency_list6 = []
        result6 = 0
        self.assertEqual(adjacency_list6, result6)

    def test_rand_cont7(self):
        adjacency_list7 = [(1,1)]
        result7 = 0
        self.assertEqual(adjacency_list7, result7)

    def test_rand_cont8(self):
        adjacency_list8 = [(1,2), (2,3), (3,4), (4,5), (5,1), (2,6),
                           (6,7), (7,8), (8,2), (3,9), (9,10), (10,4)]
        result8 = 2
        self.assertEqual(adjacency_list8, result8)