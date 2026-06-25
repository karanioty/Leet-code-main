'''11. Container With Most Water
""Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
#code link: https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        while(l<r):
            w=r-l
            h=min(height[r],height[l])
            m=max(m,w*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m
