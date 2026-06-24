'''151. Reverse Words in a String
""Exapmle:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''
# code link: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def reverseWords(self, s: str) -> str:
        s.split(" ")
        l=[]
        r=""
        for i in s:
            if i!=" ":
                r+=i
            else:
                l.append(r)
                r=""
        l.append(r)
        l1=[]
        c=0
        for i in l:
            if i!="":
                l1.append(i)
        r1=""
        for j in range(len(l1)-1,-1,-1):
            r1+=l1[j]
            if j!=0:
                r1+=" "
        return r1
