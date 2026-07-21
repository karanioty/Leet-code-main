'''771. Jewels and Stones
""Example:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
""'''
#code link: https://leetcode.com/problems/jewels-and-stones/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        k=0
        for i in jewels:
            k+=stones.count(i)
        return k
