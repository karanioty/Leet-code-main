'''35. Search Insert Position
""Example:
Input: nums = [1,3,5,6], target = 5
Output: 2
'''
#code link: https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            if target<=nums[i]:
                c=i
                break
            elif len(nums)-1==i and nums[i]<target:
                c=len(nums)

        return c
