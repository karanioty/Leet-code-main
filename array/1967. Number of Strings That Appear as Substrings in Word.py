'''1967. Number of Strings That Appear as Substrings in Word
""Example:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.'''
#code link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/?envType=problem-list-v2&envId=array
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0
        for i in patterns:
            if i in word:
                count+=1
        return count
