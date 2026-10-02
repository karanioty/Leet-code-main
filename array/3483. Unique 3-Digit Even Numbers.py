'''3483. Unique 3-Digit Even Numbers
""Example:
Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.'''
#code link: https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-10-02
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=0
        l=[]
        for i in permutations(digits,3):
            k=int("".join(map(str,i)))
            if k>99 and k%2==0 and k not  in l:
                l.append(k)
                count+=1
                print(k)
        return count
