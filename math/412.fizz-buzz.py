'''412. Fizz Buzz
""Example:
Input: n = 3
Output: ["1","2","Fizz"]'''
#code link: https://leetcode.com/problems/fizz-buzz/description/?envType=problem-list-v2&envId=math
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l
