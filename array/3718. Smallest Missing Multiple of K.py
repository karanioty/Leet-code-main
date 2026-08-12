'''3718. Smallest Missing Multiple of K
""Example:
Input: nums = [8,2,3,4,6], k = 2
Output: 10
Explanation:
The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.'''
#code link: https://leetcode.com/problems/smallest-missing-multiple-of-k/description/
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        c=k
        while(True):
            if c not in nums:
                return c
            c+=k
