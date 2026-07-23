'''2540. Minimum Common Value 
Example:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
'''
#code link: https://leetcode.com/problems/minimum-common-value/description/
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common=list(set(nums1)& set(nums2))
        common.sort()
        if common==[]:
            return -1
        else:
            return common[0]
