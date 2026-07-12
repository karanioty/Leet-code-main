'''1331. Rank Transform of an Array
""Example:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.'''
#code link: https://leetcode.com/problems/rank-transform-of-an-array/
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s={}
        b=sorted(list(set(arr)))
        for i in range(len(b)):
            s[b[i]]=i+1
        for j in range(len(arr)):
            arr[j]=s[arr[j]]
        return arr
