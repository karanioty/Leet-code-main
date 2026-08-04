'''3174. Clear Digits
""Example:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.'''
#code link: https://leetcode.com/problems/clear-digits/description/?envType=problem-list-v2&envId=string
class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        for i in s:
            if i in "1234567890":
                l.pop()
            else:
                l.append(i)
        return "".join(l)
