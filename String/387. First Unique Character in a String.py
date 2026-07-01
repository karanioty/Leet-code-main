'''387. First Unique Character in a String
""Example:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.'''
#code link: https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=-1
        for i in range(len(s)):
            if s.count(s[i])==1:
                c=i
                break
        return c
