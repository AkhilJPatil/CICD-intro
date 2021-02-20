"""
Created on 20/02/2021
@author: Akhil

automated test script for hackerrank_ds_4.py
"""
# import sys
# sys.path.append('E:/Github/CICD-intro/code')
import unittest

from CICDIntro.code.hackerrank_DS_4 import rotateLeft


class test(unittest.TestCase):
    def test_small_pos(self):
        """
        test to rotate a small array by only 1 position
        :return: 3,5,7,1
        """
        d = 1
        arr = [1,3,5,7]
        result = hrds4.rotateLeft(d, arr)
        self.assertEqual(result, [3, 5, 7, 1])


if __name__ == "main":
    unittest.main()
