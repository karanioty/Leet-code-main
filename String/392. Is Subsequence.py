'''392. Is Subsequence
""Example:
Input: s = "abc", t = "ahbgdc"
Output: true
'''
#code link: https://leetcode.com/problems/is-subsequence/description/?envType=problem-list-v2&envId=string
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while(i<len(s) and j<len(t)):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
