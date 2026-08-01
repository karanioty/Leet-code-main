'''3856. Trim Trailing Vowels
""Example:
Input: s = "idea"
Output: "id"
Explanation:
Removing "idea", we obtain the string "id".'''
#code link: https://leetcode.com/problems/trim-trailing-vowels/description/?envType=problem-list-v2&envId=string
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        k=""
        for i in range(len(s)-1,-1,-1):
            if s[i] in "aeiou":
                continue
            else:
                k=s[:i+1]
                break
        return k
