'''414. Third Maximum Number
""Example:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.'''
# code link: https://leetcode.com/problems/third-maximum-number/description/?envType=problem-list-v2&envId=array
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        b=nums[len(nums)-1]
        c=1
        d=set(nums)
        if len(d)>=3:
            for i in range(len(nums)-2,-1,-1):
                if b>nums[i]:
                    b=nums[i]
                    c+=1
                if c==3:
                    break
        else:
            b=max(nums)
        return b
