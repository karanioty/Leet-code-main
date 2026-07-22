'''2824. Count Pairs Whose Sum is Less than Target
""Example:
Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.'''
#code link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j:
                    if target>nums[i]+nums[j]:
                        count+=1
        return count
