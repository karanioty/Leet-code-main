'''3498. Reverse Degree of a String
""Example:
Input: s = "abc"

Output: 148

Explanation:

Letter	Index in Reversed Alphabet	Index in String	Product
'a'	26	1	26
'b'	25	2	50
'c'	24	3	72
The reversed degree is 26 + 50 + 72 = 148.
'''
#code link: https://leetcode.com/problems/reverse-degree-of-a-string/description/?envType=daily-question&envId=2026-09-20
class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(1,len(s)+1):
            sum+=((123-ord(s[i-1]))*i)
        return sum
