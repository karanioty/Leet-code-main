'''2529. Maximum Count of Positive Integer and Negative Integer
""Example:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.'''
#code link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=problem-list-v2&envId=array
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        c1=0
        for i in nums:
            if 0>i:
                c+=1
            elif 0<i:
                c1+=1
        return max(c,c1)
