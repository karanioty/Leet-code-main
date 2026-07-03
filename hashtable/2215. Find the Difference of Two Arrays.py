'''2215. Find the Difference of Two Arrays
""Example:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].'''
#code link: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
            else:
                l.append(i)
        return [l,list(nums2)]
