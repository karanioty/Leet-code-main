'''27. Remove Element
""Eaxmple:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).'''
#code link: https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        k=nums.count(val)
        while(i<j):
            if nums[i]==val and nums[j]!=val :
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            elif nums[j]==val:
                j-=1
            else:
                i+=1
        if k==0:
            return len(nums)
        else:
            return len(nums[:-k])
                
