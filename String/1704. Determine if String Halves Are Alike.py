'''1704. Determine if String Halves Are Alike
""Example:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
'''
#code link: https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=problem-list-v2&envId=string
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c="AEIOUaeiou"
        b=len(s)//2
        count=0
        count1=0
        print(s[:b],s[b:])
        for i in s[b:]:
            if i in c:
                count+=1
        for j in s[:b]:
            if j in c:
                count1+=1
        return count==count1
