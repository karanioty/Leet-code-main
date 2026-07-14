'''1025. Divisor Game
""Example:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.'''
#code link: https://leetcode.com/problems/divisor-game/description/?envType=problem-list-v2&envId=math
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2==0:
            return True
        return False
