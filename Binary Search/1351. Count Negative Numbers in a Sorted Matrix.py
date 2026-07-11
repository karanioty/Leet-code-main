'''1351. Count Negative Numbers in a Sorted Matrix
""Example:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.'''
#code link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    c+=1
        return c
