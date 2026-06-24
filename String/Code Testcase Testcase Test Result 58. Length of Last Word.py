'''58. Length of Last Word
"""Example:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
# code link: https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
