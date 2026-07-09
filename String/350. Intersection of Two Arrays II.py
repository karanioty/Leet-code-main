'''350. Intersection of Two Arrays II
""Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]'''
#code link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=sorting
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                l.append(i)
                nums2.remove(i)
        return l
