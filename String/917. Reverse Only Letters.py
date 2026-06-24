'''917. Reverse Only Letters
""Example:
Input: s = "ab-cd"
Output: "dc-ba"
'''
# code link: https://leetcode.com/problems/reverse-only-letters/description/?envType=problem-list-v2&envId=string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while i<j:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i].isalpha():
                j-=1
            else:
                i+=1
        return "".join(s)

            

