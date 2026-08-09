'''1281. Subtract the Product and Sum of Digits of an Integer
""Example:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15'''
#code link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        add=0
        for i in str(n):
            mul*=int(i)
            add+=int(i)
        return mul-add
