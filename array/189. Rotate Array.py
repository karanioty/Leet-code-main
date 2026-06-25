'''189. Rotate Array
""Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
#code link: https://leetcode.com/problems/rotate-array/description/?envType=problem-list-v2&envId=array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(arr,i,j):
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        def call(arr,n,s):
            rotate(arr,0,n-1)
            rotate(arr,0,s-1)
            rotate(arr,s,n-1)
            return arr
        if len(nums)>1:
            call(nums,len(nums),k%len(nums))
        
