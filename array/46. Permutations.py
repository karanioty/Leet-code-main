'''46. Permutations

""Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]'''
#code link: https://leetcode.com/problems/permutations/description/
from itertools import permutations as pi
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        l=[]
        for i in pi(nums,len(nums)):
            l.append(list(i))
        return l
