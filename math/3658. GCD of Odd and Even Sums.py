'''3658. GCD of Odd and Even Sums
""Example:
Input: n = 4
Output: 4
Explanation:
Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.'''
#code link: https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/?envType=problem-list-v2&envId=math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=1
        even=2
        o=0
        e=0
        for i in range(n):
            o+=odd
            e+=even
            odd+=2
            even+=2
        
        return gcd(o,e)
