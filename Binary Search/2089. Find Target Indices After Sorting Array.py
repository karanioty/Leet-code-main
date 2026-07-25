'''2089. Find Target Indices After Sorting Array
""Example:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.'''
#code link: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            if target==nums[i]:
                l.append(i)
        return l
