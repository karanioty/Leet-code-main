'''1979. Find Greatest Common Divisor of Array
""Example:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2...'''
# code link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        return gcd(mi,ma)
