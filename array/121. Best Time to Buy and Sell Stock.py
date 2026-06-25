'''121. Best Time to Buy and Sell Stock
""Examole:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.'''
#code link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=array
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c=prices[0]
        l=set()
        for i in range(len(prices)):
            if c>prices[i]:
                c=prices[i]
            else:
                l.add(prices[i]-c)
        return max(l)
