'''169. Majority Element
""Example:
Input: nums = [3,2,3]
Output: 3
'''
#code link: https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=array
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m={}
        for i in range(len(nums)):
            m[nums[i]]=m.get(nums[i],0)+1
        k=max(m.values())
        d=0
        for i,j in m.items():
            if j==k:
                d=i
                break
        return d
