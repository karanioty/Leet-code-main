'''3280. Convert Date to Binary
""Example:
Input: date = "2080-02-29"
Output: "100000100000-10-11101"
Explanation:
100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.'''
#code link: https://leetcode.com/problems/convert-date-to-binary/description/?envType=problem-list-v2&envId=string
class Solution:
    def convertDateToBinary(self, date: str) -> str:
       s=date.split("-")
       a=bin(int(s[0]))[2:]
       b=bin(int(s[1]))[2:]
       c=bin(int(s[2]))[2:]
       return a+"-"+b+"-"+c
