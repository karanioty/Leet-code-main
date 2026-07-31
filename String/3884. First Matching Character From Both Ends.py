'''3884. First Matching Character From Both Ends
""Example:
Input: s = "abcacbd"
Output: 1
Explanation:
At index i = 1, s[1] and s[5] are both 'b'.
No smaller index satisfies the condition, so the answer is 1.'''
#code link: https://leetcode.com/problems/first-matching-character-from-both-ends/description/?envType=problem-list-v2&envId=string
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        f=-1
        for i in range(n):
            if s[i]==s[n-i-1]:
                f=1
                return min(i,n-i-1)
        if f==-1:
            return -1
