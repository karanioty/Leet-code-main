'''42. Trapping Rain Water
""EXAMPLE:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.'''
#code link: https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def trap(self, height: list[int]) -> int:
        l=0
        r=0
        i=0
        j=len(height)-1
        w=0
        while(i<=j):
            if height[i]<=height[j]:
                if height[i]>l:
                    l=height[i]
                else:
                    w+=l-height[i]
                i+=1
            else:
                if height[j]>r:
                    r=height[j]
                else:
                    w+=r-height[j]
                j-=1
        return w
