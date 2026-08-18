'''3370. Smallest Number With All Set Bits
""Example:
Input: n = 5
Output: 7
Explanation:
The binary representation of 7 is "111".'''
# code link: https://leetcode.com/problems/smallest-number-with-all-set-bits/description/
class Solution:
    def smallestNumber(self, n: int) -> int:
        b=bin(n)[2:]
        c="1"*len(b)
        return int(c,2)
