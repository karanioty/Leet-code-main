'''5. Longest Palindromic Substring
""Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.""
'''
#code link: https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=string
class Solution:
    def longestPalindrome(self, s: str) -> str:
        r=""
        rl=0
        def rev(l,r):
            while l>=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(len(s)):
            odd=rev(i,i)
            if len(odd)>rl:
                r=odd
                rl=len(odd)
            even=rev(i,i+1)
            if len(even)>rl:
                r=even
                rl=len(even)
        return r
