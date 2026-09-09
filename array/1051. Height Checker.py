'''1051. Height Checker
""Example:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.'''
#code link: https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k = heights[:]
        count = 0
        k.sort()
        for i in range(0,len(heights)):
            if heights[i] != k[i]:
                count += 1
        return count
