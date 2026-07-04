'''338. Counting Bits
""Example:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
'''
#code link: https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=dynamic-programming
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            b=bin(i)[2:]
            l.append(b.count("1"))
        return l
