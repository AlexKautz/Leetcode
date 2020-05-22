# Leetcode question 1 - Two sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

# O(n^2) solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if (nums[i] + nums[j] == target and i != j):
#                     return [i, j]
#         return None

# O(n) solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         mymap = {}
#         #first pass adds values to a dic
#         for i in range(n):
#             mymap[nums[i]] = i
        
#         # second pass works better
#         for i in range(n):
#             want = target - nums[i]
#             index = mymap.get(want)
#             if (index != None and index != i):
#                 return [i, index]
#         return None
# Runtime: 64 ms, faster than 40.17% of Python3 online submissions for Two Sum.
# Memory Usage: 15.6 MB, less than 5.11% of Python3 online submissions for Two Sum.

# O(n) solution, one pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i in range(len(nums)):
            index = mymap.get(target - nums[i])
            if index != None and index != i:
                return [i, index]

            mymap[nums[i]] = i
        return None
# Runtime: 48 ms, faster than 78.99% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 5.11% of Python3 online submissions for Two Sum.



# print(Solution.twoSum(None, [2, 7, 11, 15], 9))
# print(Solution.twoSum(None, [3, 2, 4], 6))
print(Solution.twoSum(None, [3, 3], 6))


# Real quick now we know about Hash maps, what about Heaps?

# A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out various operations on heap data structure. Below is a list of these functions.

# heapify - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
# heappush – This function adds an element to the heap without altering the current heap.
# heappop - This function returns the smallest data element from the heap.
# heapreplace – This function replaces the smallest data element with a new value supplied in the function.