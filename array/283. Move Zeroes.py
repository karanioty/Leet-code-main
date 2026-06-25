'''283. Move Zeroes
""Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
#code link: https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=array
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
