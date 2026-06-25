'''349. Intersection of Two Arrays
""Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]'''
#code link: https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                l.append(i)
        k=list(set(l))
        return k
