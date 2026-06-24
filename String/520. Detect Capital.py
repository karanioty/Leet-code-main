'''520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 
""Example:
Input: word = "USA"
Output: true'''
# code link: https://leetcode.com/problems/detect-capital/description/?envType=problem-list-v2&envId=string
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (word.isupper() or word.islower()or word.istitle())
