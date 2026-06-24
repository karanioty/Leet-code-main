'''344. Reverse String
""Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
#code link: https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        for k in range(len(s)//2):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        
