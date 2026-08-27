'''3746. Minimum String Length After Balanced Removals
""Example:
Input: s = "aabbab"
Output: 0
Explanation:
The substring "aabbab" has three 'a' and three 'b'. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.'''
#code link: https://leetcode.com/problems/minimum-string-length-after-balanced-removals/description/?envType=problem-list-v2&envId=stack
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        s1=set(s)
        l=[]
        for i in s1:
            l.append(s.count(i))
        if len(l)==1:
            return l[0]
        else:
            return abs(min(l)-max(l))
