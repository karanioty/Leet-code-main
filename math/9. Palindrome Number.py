'''9. Palindrome Number
""Example:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
#code link: https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            b=int(str(x)[::-1])
            if b==x:
                return True
            else:
                return False
        else:
            return False
            
