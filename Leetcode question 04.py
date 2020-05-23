# Leetcode question 4 - Median of Two Sorted Arrays
import unittest
from typing import List

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

# A simple solution is to first to zip that to lists together into one sorted list O(n+m)
# Then find a median of the resulting list


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return Solution.findMedianOfList(Solution.zipSortedLists(nums1, nums2))

    @staticmethod
    def zipSortedLists(list_1: List[int], list_2: List[int]) -> List[int]:
        outList: List[int] = []
        index_1 = 0
        index_2 = 0
        length_of_list_1 = len(list_1)
        length_of_list_2 = len(list_2)

        while(index_1 < length_of_list_1 or index_2 < length_of_list_2):
            if index_1 == length_of_list_1:
                outList.append(list_2[index_2])
                index_2 += 1
            elif index_2 == length_of_list_2:
                outList.append(list_1[index_1])
                index_1 += 1
            elif list_1[index_1] < list_2[index_2]:
                outList.append(list_1[index_1])
                index_1 += 1
            else:
                outList.append(list_2[index_2])
                index_2 += 1
        
        return outList

# 1 2 3
# len = 3
# len/2 = 1.5 = 1
    @staticmethod
    def findMedianOfList(my_list: List[int]) -> float:
        length_of_list = len(my_list)
        if length_of_list % 2 == 1: # Length is odd
            return float(my_list[length_of_list // 2])
        else:
            return float((my_list[length_of_list // 2 - 1] + my_list[length_of_list // 2]) / 2)

# Runtime: 104 ms, faster than 33.28% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.2 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

# TODO Wait you can do it in O(log(min(m,n))) ???




class TestSolution(unittest.TestCase):
    def test_find_median_odd(self):
        self.assertEqual(Solution.findMedianOfList([5, 7, 22, 200, 1000]), 22)

    def test_find_median_even(self):
        self.assertEqual(Solution.findMedianOfList([5, 7, 22, 200]), 14.5)
    
    def test_zip_1(self):
        self.assertEqual(Solution.zipSortedLists([1, 5], []), [1, 5])

    def test_zip_2(self):
        self.assertEqual(Solution.zipSortedLists([], [1, 5]), [1, 5])
    
    def test_zip_3(self):
        self.assertEqual(Solution.zipSortedLists([1, 22, 57, 100], [23, 24, 25, 58]), [1, 22, 23, 24, 25, 57, 58, 100])
    
    def test_full_thing_1(self):
        self.assertEqual(Solution.findMedianSortedArrays(None, [1, 2], [3, 4]), 2.5)

    def test_full_thing_2(self):
        self.assertEqual(Solution.findMedianSortedArrays(None, [1, 3], [2]), 2)

if __name__ == "__main__":
    unittest.main()