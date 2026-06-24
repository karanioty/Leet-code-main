'''434. Number of Segments in a String
""Example:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
'''
#code link: https://leetcode.com/problems/number-of-segments-in-a-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
