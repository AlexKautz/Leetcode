import unittest
import heapq

# Leetcode question 3 - Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if s == None:
#             return None
#         if s == "":
#             return 0
#         topLengthsHeap = []

#         for j in range(len(s)):
#             letterSet = set()
#             for i in range(j, len(s)):
#                 if s[i] in letterSet:
#                     heapq.heappush(topLengthsHeap, -1*len(letterSet))
#                     break
#                 else:
#                     letterSet.add(s[i])
#             else:
#                 heapq.heappush(topLengthsHeap, -1*len(letterSet))
#         out = -1*heapq.heappop(topLengthsHeap)
#         return out

# Runtime: 516 ms, faster than 14.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 15.4 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.

# This was good, but we can do it a lot faster using the sliding window approach.
# The idea is that once part of the string has been checked, it doesn't need to be checked again.
# So we inch worm across the string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIndex = 0 # Beginning of substring
        endIndex = 0 # End of substring
        charSet = set() # Set of characters
        n = len(s)
        out = 0 # The length of the longer substring
        
        while startIndex < n and endIndex < n:
            currentChar = s[endIndex]
            if currentChar in charSet:
                charSet.remove(s[startIndex])
                out = max(out, endIndex - startIndex)
                startIndex += 1
            else:
                charSet.add(currentChar)
                endIndex += 1
                if endIndex == n:
                    out = max(out, endIndex - startIndex)

        
        return out

# Runtime: 64 ms, faster than 66.47% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.8 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.



class TestSolution(unittest.TestCase):
    def test_2(self):
        self.assertEqual(Solution.lengthOfLongestSubstring(None, ""), 0)
    
    def test_3(self):
        self.assertEqual(Solution.lengthOfLongestSubstring(None, "abc"), 3)
    
    def test_4(self):
        self.assertEqual(Solution.lengthOfLongestSubstring(None, "abcabcbb"), 3)
    
    def test_5(self):
        self.assertEqual(Solution.lengthOfLongestSubstring(None, "aab"), 2)
    
    def test_6(self):
        self.assertEqual(Solution.lengthOfLongestSubstring(None, "pwwkew"), 3)
    
    def test_7(self):
        self.assertEqual(Solution.lengthOfLongestSubstring(None, "bbbbb"), 1)

if __name__ == "__main__":
    unittest.main()
