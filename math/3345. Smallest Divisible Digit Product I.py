'''3345. Smallest Divisible Digit Product I
""Example:
Input: n = 10, t = 2
Output: 10
Explanation:
The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.'''
#code link: https://leetcode.com/problems/smallest-divisible-digit-product-i/description/?envType=problem-list-v2&envId=math
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

       while(True):
            sum=1
            for i in str(n):
                sum*=int(i)
            if sum %t==0:
                return n
            n+=1
