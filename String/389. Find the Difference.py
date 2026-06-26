'''389. Find the Difference
""Example:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.'''
#code link: https://leetcode.com/problems/find-the-difference/description/?envType=problem-list-v2&envId=string
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        i=0
        while(i<len(s)):
            if s[i] in t:
                t.remove(s[i])
                i+=1
            else:
                i+=1
        return ''.join(t)
