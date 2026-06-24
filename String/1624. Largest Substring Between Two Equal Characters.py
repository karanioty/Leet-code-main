'''1624. Largest Substring Between Two Equal Characters
""Example:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
'''
#code link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=problem-list-v2&envId=string
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        f_i={}
        ans=-1
        for i,ch in enumerate(s):
            if ch in f_i:
                ans=max(ans,i-f_i[ch]-1)
            else:
                f_i[ch]=i
        return ans
