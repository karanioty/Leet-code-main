'''3754. Concatenate Non-Zero Digits and Multiply by Sum I
""Example:
Input: n = 10203004
Output: 12340
Explanation:
The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
Therefore, the answer is x * sum = 1234 * 10 = 12340.'''
#code link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/?envType=problem-list-v2&envId=math
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        r="0"
        n1=str(n)
        for i in n1:
            if i in "123456789":
                sum+=int(i)
                r+=i
        return sum*(int(r))
