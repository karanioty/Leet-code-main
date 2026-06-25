'''3. Longest Substring Without Repeating Characters
""Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
'''
#code link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_s=set()
        l=0
        ml=0
        for i in range(len(s)):
            while s[i] in c_s:
                c_s.remove(s[l])
                l+=1
            c_s.add(s[i])
            ml=max(ml,i-l+1)
        return ml
