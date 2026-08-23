'''258. Add Digits
""Example:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.'''
#code link: https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        c=num
        while c>9:
            sum=0
            for i in str(c):
                sum+=int(i)
            c=sum
        else:
            return c
