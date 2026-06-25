'''1672. Richest Customer Wealth
""Example:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.'''
#code link:  https://leetcode.com/problems/richest-customer-wealth/description/?envType=problem-list-v2&envId=array
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=-1
        for i in accounts:
            m=max(m,sum(i))  
        return m
