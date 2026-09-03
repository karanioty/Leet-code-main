'''378. Kth Smallest Element in a Sorted Matrix
""Example:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13'''
#code link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/?envType=problem-list-v2&envId=array
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=[]
        for i in matrix:
            for j in i:
                l.append(j)
        l.sort()
        return l[k-1]
