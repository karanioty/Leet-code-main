'''1287. Element Appearing More Than 25% In Sorted Array
""Example:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6'''
#code link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=problem-list-v2&envId=array
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=0
        for i in arr:
            if arr.count(i) > count:
                count=arr.count(i)
                c=i
        return c
