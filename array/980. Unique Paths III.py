'''980. Unique Paths III
""Example:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)'''
#code link: https://github.com/karanioty/Leet-code-main/new/main/array
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count=0
        count1=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    p=i
                    k=j
                if grid[i][j]!=-1:
                    count+=1
 
        def path(i,j,solution,step):
            nonlocal count,count1
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==-1 or solution[i][j]==1:
                return False
            if grid[i][j]==2:
                if step==count:
                    count1+=1
    
            solution[i][j]=1
            path(i+1,j,solution,step+1)
            path(i,j+1,solution,step+1)
            path(i-1,j,solution,step+1)
            path(i,j-1,solution,step+1)
            solution[i][j]=0
            return False
        sol=[[0]*(len(grid[0])) for i in range(len(grid)) ]
        path(p,k,sol,1)

        return count1
