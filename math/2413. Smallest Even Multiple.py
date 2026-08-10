'''2413. Smallest Even Multiple
""Example:
Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.'''
#code link: https://leetcode.com/problems/smallest-even-multiple/description/
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return n*2
