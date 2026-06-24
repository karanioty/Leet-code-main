'''345. Reverse Vowels of a String
""Example:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
'''
#code link: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def reverseVowels(self, s: str) -> str:
        a="AEIOUaeiou"
        i=0
        j=len(s)-1
        s=list(s)
        while(i<j):
            if s[i] in a and s[j] in a:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i]  in a:
                j-=1
            elif s[j] in a:
                i+=1
            else:
                i+=1
                j-=1 
        return "".join(s)       
