'''844. Backspace String Compare
""Example:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".'''
#code link: https://leetcode.com/problems/backspace-string-compare/description/?envType=problem-list-v2&envId=stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in s:
            if i=="#":
                if not l1:
                    continue
                else:
                    l1.pop()
            else:
                l1.append(i)
        for i in t:
            if i =="#":
                if not l2:
                    continue
                else:
                    l2.pop()
            else:
                l2.append(i)
        return l1==l2
