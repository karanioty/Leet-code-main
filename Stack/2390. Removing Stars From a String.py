'''2390. Removing Stars From a String
""Example:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".'''
#code link: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=problem-list-v2&envId=stack
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)
