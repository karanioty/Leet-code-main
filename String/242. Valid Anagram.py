'''242. Valid Anagram
""Example:
Input: s = "anagram", t = "nagaram"

Output: true
'''
#code link: https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        for i in t:
            if i not in s:
                return False
            f[i]-=1
            if f[i]<0:
                return False
        return True
