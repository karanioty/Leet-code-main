'''88. Merge Sorted Array
""Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.'''
# code link: https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=nums1[:m]+nums2[:n]
        arr.sort()
        for i in range(len(arr)):
            nums1[i]=arr[i]
       
        
        
