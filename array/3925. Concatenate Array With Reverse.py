'''3925. Concatenate Array With Reverse
""Example:
Input: nums = [1,2,3]

Output: [1,2,3,3,2,1]

Explanation:

The first n elements of ans are the same as nums.

For the next n = 3 elements, each element is taken from nums in reverse order:

ans[3] = nums[2] = 3
ans[4] = nums[1] = 2
ans[5] = nums[0] = 1
Thus, ans = [1, 2, 3, 3, 2, 1].''''
#code link: https://leetcode.com/problems/concatenate-array-with-reverse/description/
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=nums[::-1]
        return nums+a
