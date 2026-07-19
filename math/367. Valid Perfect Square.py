'''367. Valid Perfect Square
""Example:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.'''
#code link: https://leetcode.com/problems/valid-perfect-square/description/?envType=problem-list-v2&envId=binary-search
 class Solution:
    def isPerfectSquare(self, num: int) -> bool:
       b=int(num**0.5)
       return b*b==num
     
 
