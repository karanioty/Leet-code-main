'''575. Distribute Candies
""Example:
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.'''
#code link: https://leetcode.com/problems/distribute-candies/description/?envType=problem-list-v2&envId=array
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        l=set(candyType)
        if n==len(l):
            return n
        elif n>len(l):
            return len(l)
        else:
            return n
