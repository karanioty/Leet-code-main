'''20. Valid Parentheses
""Example:
Input: s = "()"
Output: true'''
#code link: https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack
class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        l=[]
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if len(l)==0:
                    return False
                else:
                    top=l.pop()
                    if (i=="}"and top!="{") or (i==")" and top !="(")or(i=="]" and top!="["):
                        return False
        else:
            if len(l)==0:
                return True
            else:
                return False
