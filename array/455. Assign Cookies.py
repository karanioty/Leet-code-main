'''455. Assign Cookies
""Example:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.'''
# code link: https://leetcode.com/problems/assign-cookies/description/?envType=problem-list-v2&envId=array
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        while(i<len(g) and j<len(s)):
            if g[i]<=s[j]:
                i+=1
            j+=1
        return i
