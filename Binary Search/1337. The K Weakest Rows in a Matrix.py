'''1337. The K Weakest Rows in a Matrix
""Example:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].'''
#code link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[]
        for i,j in enumerate(mat):
            l.append((sum(j),i))
        l.sort()
        return [b for a,b in l[:k]]
            
            
        
