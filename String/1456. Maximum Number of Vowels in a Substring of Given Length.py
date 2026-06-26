'''1456. Maximum Number of Vowels in a Substring of Given Length
""Example:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
'''
#code link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=problem-list-v2&envId=string
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        v="aeiou"
        for i in range(k):
            if s[i] in v:
                count+=1
        m=count
        for j in range(k,len(s)):
            if s[j] in v:
                count+=1
            if s[j-k] in v:
                count-=1
            m=max(m,count)
            if m==k:
                return m
        return m