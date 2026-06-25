'''268. Missing Number
""Example:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.'''
#code link: https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        m=0
        for i in range(len(nums)):
            if c==nums[i]:
                c+=1
            else:
                m=c
                break
        return c
