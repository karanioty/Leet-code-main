'''75. Sort Colors
""Eaxmple:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''
#code link: https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=array
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
