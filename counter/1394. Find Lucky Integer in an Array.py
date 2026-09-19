'''1394. Find Lucky Integer in an Array
""Example:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.'''
#code link: https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=problem-list-v2&envId=counting
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        m=-1
        for i in set(arr):
            if i == arr.count(i):
                m=max(m,i)
        return m
