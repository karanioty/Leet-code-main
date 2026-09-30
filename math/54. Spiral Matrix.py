'''54. Spiral Matrix
""Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]'''
#code link: https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left=0
        right=len(matrix[0])-1
        top=0
        bottum=len(matrix)-1
        l=[]
        while(left<=right and top<=bottum):
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for j in range(top,bottum+1):
                l.append(matrix[j][right])
            right-=1
            if  top<=bottum:
                for i in range(right,left-1,-1):
                    l.append(matrix[bottum][i])
                bottum-=1
            if left<=right:
                for j in range(bottum,top-1,-1):
                    l.append(matrix[j][left])
                left+=1
        return l
      
