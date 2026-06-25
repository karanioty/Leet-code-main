'''217. Contains Duplicate
""Example:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.'''
#code link: https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
