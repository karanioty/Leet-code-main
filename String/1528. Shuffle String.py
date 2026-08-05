'''1528. Shuffle String
""Example:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.'''
#code link: https://leetcode.com/problems/shuffle-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=[0]*len(s)
        for i in range(len(s)):
            l[indices[i]]=s[i]
        return "".join(l)
            
