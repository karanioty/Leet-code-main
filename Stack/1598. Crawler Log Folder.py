'''1598. Crawler Log Folder
""Example:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
'''
#code link: https://leetcode.com/problems/crawler-log-folder/description/?envType=problem-list-v2&envId=stack
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        l=[]
        for i in logs:
            if i=="../":
                if not l:
                    continue
                else:
                    l.pop()
            elif i=="./":
                continue
            else:
                l.append(i)
        return len(l)
