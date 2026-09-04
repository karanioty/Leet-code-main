'''260. Single Number III
""Example:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.'''
#code link: https://leetcode.com/problems/single-number-iii/description/?envType=problem-list-v2&envId=array
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if nums.count(i)==1 and len(l)<=2:
                l.append(i)
            if len(l)==2:
                return l
        return l
