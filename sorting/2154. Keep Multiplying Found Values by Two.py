'''2154. Keep Multiplying Found Values by Two
""Example:
Input: nums = [5,3,6,1,12], original = 3
Output: 24
Explanation: 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.'''
#code link: https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=problem-list-v2&envId=sorting
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while(True):
            if original in nums:
                original*=2
            else:
                return original
