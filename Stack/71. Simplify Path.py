'''71. Simplify Path
""Example:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).'''
#code link: https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        s=path.split("/")
        l=[]
        for i in s:
            if i=="..":
                if not l:
                    continue
                else:
                    l.pop()
            elif i =="." or i=="":
                continue
            else:
                l.append(i)
        return "/"+"/".join(l)
