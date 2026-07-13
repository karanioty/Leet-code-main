'''190. Reverse Bits
""Eaxmple:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000'''
#code link: https://leetcode.com/problems/reverse-bits/description/?envType=problem-list-v2&envId=bit-manipulation
class Solution:
    def reverseBits(self, n: int) -> int:
        c=str(bin(n)[2:])
        c1=abs(len(c)-32)
        c2="0"*c1+c
        d=c2[::-1]
        k=int(d,2)
        return k
