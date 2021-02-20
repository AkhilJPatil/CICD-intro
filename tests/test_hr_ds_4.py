"""
Created on 20/02/2021
@author: Akhil

automated test script for hackerrank_ds_4.py
"""

from code import hackerrank_DS_4  #as hrds4
import unittest


class test(unittest.TestCase):

    def test_small_pos(self):
        """
        test to rotate a small array by only 1 position
        :return: 3,5,7,1
        """
        d = 1
        arr = [1,3,5,7]
        result = hackerrank_DS_4.rotateLeft(d, arr)
        self.assertEqual(result, [3, 5, 7, 1])

    def test_med_pos5(self):
        """
        test to rotate a medium array by 5 position
        :return:
        """
        d = 5
        arr = list(i for i in range(11,25))  # list from 11 to 24
        result = hackerrank_DS_4.rotateLeft(d, arr)
        self.assertEqual(result, [16, 17, 18, 19, 20, 21, 22, 23, 24, 11, 12, 13, 14, 15])

if __name__ == "main":
    print("code start")
    unittest.main()

