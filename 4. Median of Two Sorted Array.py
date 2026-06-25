'''4. Median of Two Sorted Arrays
""Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.'''
#code link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=array
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        if len(nums)%2==1:
            return float(nums[(len(nums))//2])
        else:
            return (nums[n//2-1]+nums[n//2])/2
