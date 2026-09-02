'''215. Kth Largest Element in an Array
""Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5'''
#code link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(sorted(set(nums)))
        return sorted(nums)[-k]
