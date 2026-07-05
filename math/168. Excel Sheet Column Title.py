'''168. Excel Sheet Column Title
""Example:
Input: columnTitle = "AB"
Output: 28
'''
#code link: leetcode.com/problems/excel-sheet-column-number/?envType=problem-list-v2&envId=math
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        b=0
        for i in columnTitle:
            b=b*26+(ord(i)-64)
        return b
