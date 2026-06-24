'''28. Find the Index of the First Occurrence in a String
""Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''
#code link:https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
