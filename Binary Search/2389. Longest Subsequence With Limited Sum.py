'''2389. Longest Subsequence With Limited Sum
""Example:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.'''
#code link: https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        a=[0]*len(nums)
        nums.sort()
        a[0]=nums[0]
        for i in range(1,len(nums)):
            a[i]=a[i-1]+nums[i]
        for i in range(len(queries)):
            count=0
            for j in a:
                if j<=queries[i]:
                    count+=1
            queries[i]=count
        return queries
