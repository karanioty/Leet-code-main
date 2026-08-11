'''2652. Sum Multiples
""Example:
Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.'''
#code link: https://leetcode.com/problems/sum-multiples/description/
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s=0
        for i in range(3,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                s+=i
        return s
