'''1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
""Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
'''
#code link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        sum=0
        for i in range(k):
            sum+=arr[i]
        if sum//k>= threshold:
            count+=1
        l=0
        for i in range(k,len(arr)):
            sum-=arr[l]
            l+=1
            sum+=arr[i]
            if sum//k>=threshold:
                count+=1
        return count
