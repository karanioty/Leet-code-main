'''2144. Minimum Cost of Buying Candies With Discount
""Example:
Input: cost = [1,2,3]
Output: 5
Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.'''
# code link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/?envType=problem-list-v2&envId=array
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        b=cost[::-1]
        c=0
        s=0
        for i in b:
            
            if c!=2:
                s+=i
                c+=1
            else:
                c=0
        return s
