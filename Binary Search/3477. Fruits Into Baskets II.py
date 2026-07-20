'''3477. Fruits Into Baskets II
""Example:
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:
fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.'''
#code link: https://leetcode.com/problems/fruits-into-baskets-ii/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i=0
        j=0
        count=0
        while(i<len(fruits) and j<len(fruits)):
            if fruits[i]<=baskets[j] and baskets[j]!=-1:
                i+=1
                baskets[j]=-1
                j=0
            else:
                j+=1
            if j==len(fruits):
                i+=1
                j=0
        return abs(baskets.count(-1)-len(fruits))
            
