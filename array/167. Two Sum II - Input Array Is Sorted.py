'''167. Two Sum II - Input Array Is Sorted.py
""Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].'''
#code link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=array
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if target==numbers[i]+numbers[j]:
                return i+1,j+1
                break
            elif target<numbers[i]+numbers[j]:
                j-=1
            elif target>numbers[i]+numbers[j]:
                i+=1 
            else:
                i+=1
                j-=1
