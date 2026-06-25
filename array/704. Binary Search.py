'''704. Binary Search
""Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4'''
#code link: https://leetcode.com/problems/binary-search/description/?envType=problem-list-v2&envId=array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c=-1
        for i in range(len(nums)):
            if target==nums[i]:
                c=i
                break
        return c
