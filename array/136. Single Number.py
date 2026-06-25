'''136. Single Number
""Example:
Input: nums = [2,2,1]
Output: 1
'''
#code link: https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=array
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       for i in nums:
         if nums.count(i)==1:
            return i
