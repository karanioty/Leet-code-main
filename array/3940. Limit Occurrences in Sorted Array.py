'''3940. Limit Occurrences in Sorted Array
""Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,1,2,2,3]
Explanation:
Each element can appear at most 2 times.
The element 1 appears 3 times, so only 2 occurrences are kept.
The element 2 appears 2 times, so both occurrences are kept.
The element 3 appears 1 time, so it is kept.
Thus, the resulting array is [1, 1, 2, 2, 3].'''
#code link: https://leetcode.com/problems/limit-occurrences-in-sorted-array/description/?envType=problem-list-v2&envId=array
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        l=[]
        for i in nums:
            if l.count(i)<k:
                l.append(i)
        return l
