'''485. Max Consecutive Ones
""Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''
#code link: https://leetcode.com/problems/max-consecutive-ones/description/?envType=problem-list-v2&envId=array
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=1
        b=set()
        c=0

        for i in range(0,len(nums)):
            if a==nums[i]:
                c+=1
            else:
                b.add(c)
                c=0
        b.add(c)
        if len(b)==0:
            return 0
        else:
            return max(b)
          
