'''https://download-cdn.jetbrains.com/python/pycharm-2026.1.3.exe
""Example:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.'''""
#code link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=problem-list-v2&envId=string
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        co=0
        for i in range(k):
            if blocks[i]=="W":
                co+=1
        m=co
        for j in range(1,len(blocks)-k+1):
            if blocks[j+k-1]=="W":
                co+=1
            if blocks[j-1]=="W":
                co-=1
            m=min(m,co)
        return m
