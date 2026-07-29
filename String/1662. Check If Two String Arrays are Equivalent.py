'''1662. Check If Two String Arrays are Equivalent
""Example:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.'''
#code link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/?envType=problem-list-v2&envId=string
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        r=""
        for i in word1:
            r+=i
        r1=""
        for j in word2:
            r1+=j
        return r==r1
